import logging
from collections import defaultdict
from pathlib import Path

import chardet

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


class util:
    def __init__(self):
        pass

    @staticmethod
    def detect_encoding(file: str | Path) -> str | None:
        with open(file, "rb") as f:
            return chardet.detect(f.read(1024))["encoding"]

    @staticmethod
    def real_digit(string: str):
        try:
            int(string)
            return True
        except Exception:
            return False


class darkest:
    def __init__(
        self,
        data: dict[
            str,
            list[
                dict[
                    str,
                    list[str]
                    | int
                    | bool
                    | None
                    | str
                    | tuple[str | bool | int, str | bool | int],
                ]
            ],
        ],
    ):
        self.data: dict[
            str,
            list[
                dict[
                    str,
                    list[str]
                    | int
                    | bool
                    | str
                    | tuple[str | bool | int, str | bool | int]
                    | None,
                ]
            ],
        ] = data

    @staticmethod
    def is_number_and_percent_str(s: str):
        for char in s:
            if not (char.isdigit() or char == "%"):
                return False
        return True

    @staticmethod
    def paser(file: str | Path):
        logger.debug(f"pasering: {file}")
        data: dict[
            str,
            list[
                dict[
                    str,
                    list[str]
                    | int
                    | bool
                    | None
                    | str
                    | tuple[str | bool | int, str | bool | int],
                ]
            ],
        ] = defaultdict(list)
        encoding = util.detect_encoding(file)
        logger.debug(f"encoding: {encoding}")
        if not encoding:
            print(f"error file encoding: {file}")
            return False
        primary_key = None
        primary_value: dict[
            str,
            list[str]
            | int
            | bool
            | None
            | str
            | tuple[str | bool | int, str | bool | int],
        ] = defaultdict(list)
        content = Path(file).read_text(errors="ignore")
        for line in content.split("\n"):
            line = line.split("//")[0]
            if not len(line.strip()):
                continue
            if ":" in line:
                if primary_key is None:
                    if primary_value != {}:
                        raise ValueError(f"primary key not found: {file}:{primary_key}")
                else:
                    data[primary_key].append(primary_value)
                logger.debug(f"primary key: {primary_key}, value: {primary_value}")
                primary_key = line.split(":")[0].strip()
                logger.debug(f"add primary key: {primary_key}")
                line = line.split(":")[1]
                primary_value: dict[
                    str,
                    list[str]
                    | int
                    | bool
                    | None
                    | str
                    | tuple[str | bool | int, str | bool | int],
                ] = defaultdict(list)

            def get_secondary_dict(line: str):
                secondary_dict: dict[
                    str,
                    list[str]
                    | int
                    | bool
                    | None
                    | str
                    | tuple[str | bool | int, str | bool | int],
                ] = defaultdict(list)
                secondary_key: str | None = None
                secondary_values: list[str | bool | int] = []

                def format_value(value: list[str | bool | int]):
                    if len(value) == 0:
                        return None
                    elif len(value) == 1:
                        return secondary_values[0]
                    elif len(value) == 2:
                        return (secondary_values[0], secondary_values[1])
                    else:
                        return [str(item) for item in secondary_values]

                sections = line
                for section in sections.split():
                    if not len(section.strip()):
                        continue

                    if section.startswith(
                        "."
                    ) and not darkest.is_number_and_percent_str(section.strip(".")):
                        if secondary_key is None:
                            pass
                        else:
                            secondary_dict[secondary_key] = format_value(
                                secondary_values
                            )
                            secondary_values: list[str | bool | int] = []
                            logger.debug(
                                f"add secondary key: {section}, values: {secondary_dict[secondary_key]}"
                            )
                        secondary_key = section.strip(".")
                        logger.debug(f"found secondary key: {section}")
                    else:
                        if secondary_key is None:
                            print("Invalid", section, file, line)
                        else:
                            logger.debug(f"found secondary value: {section}")
                            if section.lower() == "true":
                                secondary_values.append(True)
                            elif section.lower() == "false":
                                secondary_values.append(False)
                            elif util.real_digit(section):
                                secondary_values.append(int(section))
                            else:
                                secondary_values.append(section.strip('"').strip("'"))
                if secondary_key is None:
                    pass
                else:
                    secondary_dict[secondary_key] = format_value(secondary_values)
                return secondary_dict

            logger.debug(f"found secondary value: {line}")
            secondary_dict = get_secondary_dict(line)
            primary_value.update(secondary_dict)
        if primary_key is not None:
            data[primary_key].append(primary_value)
        return darkest(data)
