from pathlib import Path
from typing import Callable

from DarkestDungeonClass.darkest import file_parser
from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.file.buff import buff_file
from DarkestDungeonClass.dd_game_type.file.loot import loot_file
from DarkestDungeonClass.dd_game_type.file.trait import trait_file
from DarkestDungeonClass.util import xml_data


class mod:
    def __init__(self, mod_path: str | Path):
        self.mod_path = Path(mod_path)
        self.xml_info: xml_data
        self.dataModel_regexFile: dict[Callable[[str], BaseModel], list[str]] = {}
        self.data_map: dict[Path, BaseModel] = {}
        self.effect_map: dict[Path, list[type]] = {}
        self.hero_map: dict[Path, list[type]] = {}
        self.buff_map: dict[Path, list[type]] = {}
        self.loot_map: dict[Path, list[type]] = {}
        self.trait_map: dict[Path, list[type]] = {}

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
        self.dataModel_regexFile = {
            buff_file.model_validate_json: [
                "shared/buffs/*.json",
                "dlc/*/shared/buffs/*.json",
                "dlc/*/features/*/shared/buffs/*.json",
            ],
            loot_file.model_validate_json: [
                "loot/*.json",
                "dlc/*/loot/*.json",
                "dlc/*/features/*/loot/*.json",
            ],
            trait_file.model_validate_json: [
                "shared/trait/*.json",
                "dlc/*/shared/trait/*.json",
                "dlc/*/features/*/shared/trait/*.json",
            ],
            file_parser("effect").darkest_paser: [
                "effects/*.darkest",
                "modes/*/effects/*.darkest",
                "dlc/*/effects/*.darkest",
                "dlc/*/modes/*/effects/*.darkest",
                "dlc/*/features/*/effects/*.darkest",
                "dlc/*/features/*/modes/*/effects/*.darkest",
            ],
            file_parser("hero_info").darkest_paser: [
                "heroes/*/*info.darkest",
                "heroes/*/*override.darkest",
                "dlc/*/heroes/*/*info.darkest",
                "dlc/*/heroes/*/*override.darkest",
                "dlc/*/features/*/heroes/*/*info.darkest",
                "dlc/*/features/*/heroes/*/*override.darkest",
            ],
        }

        for k, v in self.dataModel_regexFile.items():
            for i in v:
                if i.endswith("*.json"):
                    for file in self.mod_path.glob(i):
                        self.data_map[file] = k(
                            file.read_text(encoding="utf-8", errors="ignore")
                        )
                if i.endswith("*.darkest"):
                    for file in self.mod_path.glob(i):
                        self.data_map[file] = k(str(file.absolute()))


class mod_manager:
    def __init__(self, mods_path: list[str | Path]):
        self.mod_path = [Path(i) for i in mods_path]
        self.mods_map = {i: mod(i) for i in self.mod_path}
