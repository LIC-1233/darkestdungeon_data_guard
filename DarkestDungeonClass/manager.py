from collections import defaultdict
from pathlib import Path
from typing import Callable

from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.effect.effect import effect
from DarkestDungeonClass.dd_game_type.file.effect import effect_file
from DarkestDungeonClass.dd_game_type.file.hero_info import hero_info_file
from DarkestDungeonClass.mod import mod


class model_regex(BaseModel):
    name: str
    dataModel: Callable[[str], BaseModel]
    regexFile: list[str]


# class mod:
#     def __init__(self, mod_path: str | Path):
#         self.mod_path = Path(mod_path)
#         self.xml_info: xml_data
#         self.dataModel_regexFile: list[tuple[dict[Path, Any], model_regex]] = []
#         self.data_map: dict[Path, BaseModel] = {}
#         self.effect_map: dict[Path, effect_file] = {}
#         self.hero_map: dict[Path, heroes_info_file] = {}
#         self.buff_map: dict[Path, buff_file] = {}
#         self.loot_map: dict[Path, loot_file] = {}
#         self.trait_map: dict[Path, trait_file] = {}

#         self.init()

#     def init(self):
#         self.xml_init()
#         self.file_init()

#     def xml_init(self):
#         if xml_files := set((self.mod_path / "project_file").glob("*.xml")) | set(
#             self.mod_path.glob("project.xml")
#         ):
#             xml_file: Path = xml_files.pop()
#             self.xml_info = xml_data.mod_xml_parser(xml_file)

#     def file_init(self):
#         self.dataModel_regexFile: list[tuple[dict[Path, Any], model_regex]] = [
#             (
#                 self.buff_map,
#                 model_regex(
#                     name="buffs",
#                     dataModel=buff_file.model_validate_json,
#                     regexFile=[
#                         "shared/buffs/*.json",
#                         "dlc/*/shared/buffs/*.json",
#                         "dlc/*/features/*/shared/buffs/*.json",
#                     ],
#                 ),
#             ),
#             (
#                 self.loot_map,
#                 model_regex(
#                     name="loot",
#                     dataModel=loot_file.model_validate_json,
#                     regexFile=[
#                         "loot/*.json",
#                         "dlc/*/loot/*.json",
#                         "dlc/*/features/*/loot/*.json",
#                     ],
#                 ),
#             ),
#             (
#                 self.trait_map,
#                 model_regex(
#                     name="trait",
#                     dataModel=trait_file.model_validate_json,
#                     regexFile=[
#                         "shared/trait/*.json",
#                         "dlc/*/shared/trait/*.json",
#                         "dlc/*/features/*/shared/trait/*.json",
#                     ],
#                 ),
#             ),
#             (
#                 self.effect_map,
#                 model_regex(
#                     name="effect",
#                     dataModel=file_parser(effect_file).darkest_paser,
#                     regexFile=[
#                         "effects/*.darkest",
#                         "modes/*/effects/*.darkest",
#                         "dlc/*/effects/*.darkest",
#                         "dlc/*/modes/*/effects/*.darkest",
#                         "dlc/*/features/*/effects/*.darkest",
#                         "dlc/*/features/*/modes/*/effects/*.darkest",
#                     ],
#                 ),
#             ),
#             (
#                 self.hero_map,
#                 model_regex(
#                     name="hero_info",
#                     dataModel=file_parser(heroes_info_file).darkest_paser,
#                     regexFile=[
#                         "heroes/*/*info.darkest",
#                         "heroes/*/*override.darkest",
#                         "dlc/*/heroes/*/*info.darkest",
#                         "dlc/*/heroes/*/*override.darkest",
#                         "dlc/*/features/*/heroes/*/*info.darkest",
#                         "dlc/*/features/*/heroes/*/*override.darkest",
#                     ],
#                 ),
#             ),
#         ]

#         for data_map, modelRegex in self.dataModel_regexFile:
#             for i in modelRegex.regexFile:
#                 if i.endswith("json"):
#                     for file in self.mod_path.glob(i):
#                         data_map[file] = modelRegex.dataModel(
#                             file.read_text(encoding="utf-8", errors="ignore")
#                         )
#                 if i.endswith("darkest"):
#                     for file in self.mod_path.glob(i):
#                         data_map[file] = modelRegex.dataModel(str(file.absolute()))


class path_entry[T](
    BaseModel,
):
    path: Path
    data: T


class mod_manager:
    def __init__(
        self,
        # mods_path: Optional[list[str | Path]],
        ordered_mod_paths: list[str | Path],
    ) -> None:
        self.ordered_mod_paths: list[Path] = []
        self.ordered_mod_paths = [Path(i) for i in ordered_mod_paths]

        self.init()

    def init(self) -> None:
        self.mods_map: dict[Path, mod]
        self.mods_init()
        self.map_init()

    def mods_init(self) -> None:
        self.mods_map: dict[Path, mod] = {i: mod(i) for i in self.ordered_mod_paths}
        self.effects: list[path_entry[effect_file]] = [
            path_entry[effect_file](path=effect_map.path, data=effect_map.data)
            for mod_ in self.mods_map.values()
            for effect_map in mod_.effects.data_maps
        ]
        self.heroes: list[path_entry[hero_info_file]] = [
            path_entry[hero_info_file](path=hero_map.path, data=hero_map.data)
            for mod_ in self.mods_map.values()
            for hero_map in mod_.heroes.data_maps
        ]

    def map_init(self) -> None:
        self.effectId_pathEntries: dict[str, list[path_entry[effect]]] = defaultdict(
            list
        )  # TODO 只应该在初始化时使用，后续在其他类的映射里修改
        self.hero_id_map: dict[str, list[path_entry[hero_info_file]]] = defaultdict(
            list
        )
        for effect_path_entry in self.effects:
            for effect_ in effect_path_entry.data.effect:
                self.effectId_pathEntries[effect_.name].append(
                    path_entry[effect](path=effect_path_entry.path, data=effect_)
                )
        for hero_path_entry in self.heroes:
            self.hero_id_map[hero_path_entry.path.parent.name].append(
                path_entry[hero_info_file](
                    path=hero_path_entry.path, data=hero_path_entry.data
                )
            )
        # self.hero_inner_map_init()

    def hero_inner_map_init(self):
        for heros in self.hero_id_map.values():
            for hero_path_entry in heros:
                _hero_path = hero_path_entry.path
                hero_obj = hero_path_entry.data
                if hero_obj.crit.effects:
                    for effect_index in range(len(hero_obj.crit.effects)):
                        effect_id = hero_obj.crit.effects[effect_index]
                        if (
                            isinstance(effect_id, str)
                            and effect_id in self.effectId_pathEntries
                        ):
                            hero_obj.crit.effects[effect_index] = (
                                self.effectId_pathEntries[effect_id][0].data
                            )
                for combat_skill_ in hero_obj.combat_skill:
                    if combat_skill_.effect:
                        for effect_index in range(len(combat_skill_.effect)):
                            effect_id = combat_skill_.effect[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effectId_pathEntries
                            ):
                                combat_skill_.effect[effect_index] = (
                                    self.effectId_pathEntries[effect_id][0].data
                                )
                for deaths_door_ in hero_obj.deaths_door:
                    if deaths_door_.enter_effects:
                        for effect_index in range(len(deaths_door_.enter_effects)):
                            effect_id = deaths_door_.enter_effects[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effectId_pathEntries
                            ):
                                deaths_door_.enter_effects[effect_index] = (
                                    self.effectId_pathEntries[effect_id][0].data
                                )
                for hp_reaction_ in hero_obj.hp_reaction:
                    if hp_reaction_.effects:
                        for effect_index in range(len(hp_reaction_.effects)):
                            effect_id = hp_reaction_.effects[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effectId_pathEntries
                            ):
                                hp_reaction_.effects[effect_index] = (
                                    self.effectId_pathEntries[effect_id][0].data
                                )
                for death_reaction_ in hero_obj.death_reaction:
                    if death_reaction_.effects:
                        for effect_index in range(len(death_reaction_.effects)):
                            effect_id = death_reaction_.effects[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effectId_pathEntries
                            ):
                                death_reaction_.effects[effect_index] = (
                                    self.effectId_pathEntries[effect_id][0].data
                                )