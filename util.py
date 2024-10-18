from collections import defaultdict
from pathlib import Path


class monster:
    def __init__(self, data: dict[str, list[dict[str, list[str]]]]):
        self._data = data

    @staticmethod
    def paser_darkest(file: str | Path):
        data: dict[str, list[dict[str, list[str]]]] = defaultdict(list)
        content = Path(file).read_text()
        for line in content.replace("\t", "\n").split("\n"):
            primary_key: str = line.split(":")[0]
            secondary_key: list[dict[str, list[str]]] = []
            line = line.split(":")[1]
            for section in line.split("."):
                if not len(section.strip()):
                    continue
                sections = section.split()
                secondary_key.append(
                    {sections[0]: [i.strip('"') for i in sections[1:]]}
                )
            data[primary_key] += secondary_key
        return monster(data)
