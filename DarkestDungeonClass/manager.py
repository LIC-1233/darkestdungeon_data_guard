from collections import defaultdict
from pathlib import Path
from typing import Any, Callable

from DarkestDungeonClass.darkest import file_parser
from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.effect.effect import effect
from DarkestDungeonClass.dd_game_type.file.buff import buff_file
from DarkestDungeonClass.dd_game_type.file.effect import effect_file
from DarkestDungeonClass.dd_game_type.file.hero_info import heroes_info_file
from DarkestDungeonClass.dd_game_type.file.loot import loot_file
from DarkestDungeonClass.dd_game_type.file.trait import trait_file
from DarkestDungeonClass.util import xml_data


class model_regex(BaseModel):
    name: str
    dataModel: Callable[[str], BaseModel]
    regexFile: list[str]


class mod:
    def __init__(self, mod_path: str | Path):
        self.mod_path = Path(mod_path)
        self.xml_info: xml_data
        self.dataModel_regexFile: list[tuple[dict[Path, Any], model_regex]] = []
        self.data_map: dict[Path, BaseModel] = {}
        self.effect_map: dict[Path, effect_file] = {}
        self.hero_map: dict[Path, heroes_info_file] = {}
        self.buff_map: dict[Path, buff_file] = {}
        self.loot_map: dict[Path, loot_file] = {}
        self.trait_map: dict[Path, trait_file] = {}

        self.init()

    def init(self):
        self.xml_init()
        self.file_init()

    def xml_init(self):
        if xml_files := set((self.mod_path / "project_file").glob("*.xml")) | set(
            self.mod_path.glob("project.xml")
        ):
            xml_file: Path = xml_files.pop()
            self.xml_info = xml_data.mod_xml_parser(xml_file)

    def file_init(self):
        self.dataModel_regexFile: list[tuple[dict[Path, Any], model_regex]] = [
            (
                self.buff_map,
                model_regex(
                    name="buffs",
                    dataModel=buff_file.model_validate_json,
                    regexFile=[
                        "shared/buffs/*.json",
                        "dlc/*/shared/buffs/*.json",
                        "dlc/*/features/*/shared/buffs/*.json",
                    ],
                ),
            ),
            (
                self.loot_map,
                model_regex(
                    name="loot",
                    dataModel=loot_file.model_validate_json,
                    regexFile=[
                        "loot/*.json",
                        "dlc/*/loot/*.json",
                        "dlc/*/features/*/loot/*.json",
                    ],
                ),
            ),
            (
                self.trait_map,
                model_regex(
                    name="trait",
                    dataModel=trait_file.model_validate_json,
                    regexFile=[
                        "shared/trait/*.json",
                        "dlc/*/shared/trait/*.json",
                        "dlc/*/features/*/shared/trait/*.json",
                    ],
                ),
            ),
            (
                self.effect_map,
                model_regex(
                    name="effect",
                    dataModel=file_parser("effect").darkest_paser,
                    regexFile=[
                        "effects/*.darkest",
                        "modes/*/effects/*.darkest",
                        "dlc/*/effects/*.darkest",
                        "dlc/*/modes/*/effects/*.darkest",
                        "dlc/*/features/*/effects/*.darkest",
                        "dlc/*/features/*/modes/*/effects/*.darkest",
                    ],
                ),
            ),
            (
                self.hero_map,
                model_regex(
                    name="hero_info",
                    dataModel=file_parser("hero_info").darkest_paser,
                    regexFile=[
                        "heroes/*/*info.darkest",
                        "heroes/*/*override.darkest",
                        "dlc/*/heroes/*/*info.darkest",
                        "dlc/*/heroes/*/*override.darkest",
                        "dlc/*/features/*/heroes/*/*info.darkest",
                        "dlc/*/features/*/heroes/*/*override.darkest",
                    ],
                ),
            ),
        ]

        for data_map, modelRegex in self.dataModel_regexFile:
            for i in modelRegex.regexFile:
                if i.endswith("json"):
                    for file in self.mod_path.glob(i):
                        data_map[file] = modelRegex.dataModel(
                            file.read_text(encoding="utf-8", errors="ignore")
                        )
                if i.endswith("darkest"):
                    for file in self.mod_path.glob(i):
                        data_map[file] = modelRegex.dataModel(str(file.absolute()))


class mod_manager:
    def __init__(
        self,
        # mods_path: Optional[list[str | Path]],
        ordered_mod_paths: list[str | Path],
    ) -> None:
        self.mod_paths: list[Path] = []
        self.mod_paths = [Path(i) for i in ordered_mod_paths]

        self.init()

    def init(self) -> None:
        self.mods_map: dict[Path, mod]
        self.mods_init()
        self.map_init()

    def mods_init(self) -> None:
        self.mods_map: dict[Path, mod] = {i: mod(i) for i in self.mod_paths}
        self.effects: list[tuple[Path, effect]] = [
            (effect_path, effect)
            for mod_ in self.mods_map.values()
            for effect_path, effect_file in mod_.effect_map.items()
            for effect in effect_file.effect
        ]
        self.heroes: list[tuple[Path, heroes_info_file]] = [
            (hero_path, hero_file)
            for mod_ in self.mods_map.values()
            for hero_path, hero_file in mod_.hero_map.items()
        ]

    def map_init(self) -> None:
        self.effect_id_map: dict[str, list[tuple[Path, effect]]] = defaultdict(
            list
        )  # TODO 只应该在初始化时使用，后续在其他类的映射里修改
        self.hero_id_map: dict[str, list[tuple[Path, heroes_info_file]]] = defaultdict(
            list
        )
        for effect_path, effect_ in self.effects:
            self.effect_id_map[effect_.name].append((effect_path, effect_))
        for hero_path, hero_ in self.heroes:
            self.hero_id_map[hero_path.parent.name].append((hero_path, hero_))
        self.hero_inner_map_init()

    def hero_inner_map_init(self):
        for heros in self.hero_id_map.values():
            for _hero_path, hero_obj in heros:
                for crit_ in hero_obj.crit:
                    if crit_.effects:
                        for effect_index in range(len(crit_.effects)):
                            effect_id = crit_.effects[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effect_id_map
                            ):
                                crit_.effects[effect_index] = self.effect_id_map[
                                    effect_id
                                ][0][1]
                for combat_skill_ in hero_obj.combat_skill:
                    if combat_skill_.effect:
                        for effect_index in range(len(combat_skill_.effect)):
                            effect_id = combat_skill_.effect[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effect_id_map
                            ):
                                combat_skill_.effect[effect_index] = self.effect_id_map[
                                    effect_id
                                ][0][1]
                for deaths_door_ in hero_obj.deaths_door:
                    if deaths_door_.enter_effects:
                        for effect_index in range(len(deaths_door_.enter_effects)):
                            effect_id = deaths_door_.enter_effects[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effect_id_map
                            ):
                                deaths_door_.enter_effects[effect_index] = (
                                    self.effect_id_map[effect_id][0][1]
                                )
                for hp_reaction_ in hero_obj.hp_reaction:
                    if hp_reaction_.effects:
                        for effect_index in range(len(hp_reaction_.effects)):
                            effect_id = hp_reaction_.effects[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effect_id_map
                            ):
                                hp_reaction_.effects[effect_index] = self.effect_id_map[
                                    effect_id
                                ][0][1]
                for death_reaction_ in hero_obj.death_reaction:
                    if death_reaction_.effects:
                        for effect_index in range(len(death_reaction_.effects)):
                            effect_id = death_reaction_.effects[effect_index]
                            if (
                                isinstance(effect_id, str)
                                and effect_id in self.effect_id_map
                            ):
                                death_reaction_.effects[effect_index] = (
                                    self.effect_id_map[effect_id][0][1]
                                )