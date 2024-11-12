from pathlib import Path
from typing import Any, Callable, Generic, TypeVar

from pydantic import BaseModel, Field

from DarkestDungeonClass.darkest import file_parser
from DarkestDungeonClass.dd_game_type.file.buff import buff_file
from DarkestDungeonClass.dd_game_type.file.effect import effect_file
from DarkestDungeonClass.dd_game_type.file.hero_info import hero_info_file
from DarkestDungeonClass.dd_game_type.file.loot import loot_file
from DarkestDungeonClass.dd_game_type.file.trait import trait_file
from DarkestDungeonClass.util import xml_data

T = TypeVar("T")


class data_map(BaseModel, Generic[T]):
    path: Path
    data: T


class model_regex(BaseModel, Generic[T]):
    name: str
    dataModel: Callable[[str], T]
    regexFile: list[str]
    data_maps: list[data_map[T]] = []

    def init(self, mod_path: Path):
        self.data_maps = []
        for i in self.regexFile:
            if i.endswith("json"):
                for file in mod_path.glob(i):
                    self.data_maps.append(
                        data_map[T](
                            path=file,
                            data=self.dataModel(
                                file.read_text(encoding="utf-8", errors="ignore")
                            ),
                        )
                    )
            if i.endswith("darkest"):
                for file in mod_path.glob(i):
                    self.data_maps.append(
                        data_map[T](
                            path=file, data=self.dataModel(str(file.absolute()))
                        )
                    )


class file_manager:
    mod_paths: list[Path]
    mod_files: list["mod_file"]


class mod_file:
    mod_path: Path = Field(default=None)
    xml_info: xml_data = Field(default=None)
    effects: model_regex[effect_file] = Field(default=None)
    hero_info: model_regex[hero_info_file] = Field(default=None)
    buffs: model_regex[buff_file] = Field(default=None)
    loots: model_regex[loot_file] = Field(default=None)
    traits: model_regex[trait_file] = Field(default=None)

    def __init__(self, mod_path: str | Path, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.mod_path = Path(mod_path)
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
        self.effects: model_regex[effect_file] = model_regex(
            name="effect",
            dataModel=file_parser(effect_file).darkest_paser,
            regexFile=[
                "effects/*.darkest",
                "modes/*/effects/*.darkest",
                "dlc/*/effects/*.darkest",
                "dlc/*/modes/*/effects/*.darkest",
                "dlc/*/features/*/effects/*.darkest",
                "dlc/*/features/*/modes/*/effects/*.darkest",
            ],
        )
        self.hero_info: model_regex[hero_info_file] = model_regex(
            name="hero_info",
            dataModel=file_parser(hero_info_file).darkest_paser,
            regexFile=[
                "heroes/*/*info.darkest",
                "heroes/*/*override.darkest",
                "dlc/*/heroes/*/*info.darkest",
                "dlc/*/heroes/*/*override.darkest",
                "dlc/*/features/*/heroes/*/*info.darkest",
                "dlc/*/features/*/heroes/*/*override.darkest",
            ],
        )
        self.hero_art: model_regex[hero_info_file] = model_regex(
            name="hero_info",
            dataModel=file_parser(hero_info_file).darkest_paser,
            regexFile=[
                "heroes/*/*art.darkest",
                "dlc/*/heroes/*/*art.darkest",
                "dlc/*/features/*/heroes/*/*art.darkest",
            ],
        )
        self.buffs: model_regex[buff_file] = model_regex(
            name="buff",
            dataModel=buff_file.model_validate_json,
            regexFile=[
                "shared/buffs/*.json",
                "dlc/*/shared/buffs/*.json",
                "dlc/*/features/*/shared/buffs/*.json",
            ],
        )
        self.loots: model_regex[loot_file] = model_regex(
            name="loot",
            dataModel=loot_file.model_validate_json,
            regexFile=[
                "loot/*.json",
                "dlc/*/loot/*.json",
                "dlc/*/features/*/loot/*.json",
            ],
        )
        self.traits: model_regex[trait_file] = model_regex(
            name="trait",
            dataModel=trait_file.model_validate_json,
            regexFile=[
                "shared/trait/*.json",
                "dlc/*/shared/trait/*.json",
                "dlc/*/features/*/shared/trait/*.json",
            ],
        )

        self.effects.init(self.mod_path)
        self.hero_info.init(self.mod_path)
        self.buffs.init(self.mod_path)
        self.loots.init(self.mod_path)
        self.traits.init(self.mod_path)