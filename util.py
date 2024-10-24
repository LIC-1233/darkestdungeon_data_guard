import logging
import re
from collections import defaultdict
from pathlib import Path

import chardet

logger = logging.getLogger()


class util:
    def __init__(self):
        pass

    @staticmethod
    def detect_encoding(file: str | Path) -> str | None:
        with open(file, "rb") as f:
            return chardet.detect(f.read(1024))["encoding"]

    @staticmethod
    def is_number_and_percent_str(s: str):
        for char in s:
            if not (char.isdigit() or char == "%"):
                return False
        return True

    @staticmethod
    def real_int(string: str):
        try:
            int(string)
            return True
        except Exception:
            return False

    @staticmethod
    def real_float(string: str):
        try:
            float(string)
            return True
        except Exception:
            return False


class darkest:
    class obj(str):
        pass

    def __init__(
        self,
        data: dict[
            str,
            list[dict[str, list[str | bool | int | float] | str | bool | int | float]],
        ],
        strict: bool = True,
    ):
        self.data = data
        self.__strict: bool = strict

    def __str__(self) -> str:
        if self.__strict:
            content = ""
            for p_key, p_values in self.data.items():
                for p_value in p_values:
                    content += f"{p_key}: "
                    for s_key, s_values in p_value.items():
                        content += f".{s_key} "
                        if isinstance(s_values, list):
                            for s_value in s_values:
                                content += f"{s_value} "
                        else:
                            content += f"{s_values} "
                    content += "\n"
            return content
        else:
            content = ""
            for p_key, p_values in self.data.items():
                for p_value in p_values:
                    content += f"{p_key}: "
                    for s_key, s_values in p_value.items():
                        content += f".{s_key} "
                        if not isinstance(s_values, list):
                            s_values = [s_values]
                        for s_value in s_values:
                            if isinstance(s_value, darkest.obj):
                                content += f"{s_value} "
                            elif isinstance(s_value, str):
                                content += f'"{s_value}" '
                            elif isinstance(s_value, bool):
                                content += f"{s_value} ".lower()
                            elif isinstance(s_value, int):
                                content += f"{s_value} "
                            else:
                                content += f"{s_value} "
                    content += "\n"
            return content

    @staticmethod
    def paser(s: str, strict: bool = True):
        # logger.debug(f"pasering: {s}")
        pattern = r'(?:"[^"]*"|\S+)'
        result: dict[
            str,
            list[dict[str, list[str | bool | int | float] | str | bool | int | float]],
        ] = defaultdict(list)
        current_p_key: str = ""
        current_p_value: dict[
            str, list[str | bool | int | float] | str | bool | int | float
        ] = {}
        current_s_key: str = ""
        current_s_value: list[str | bool | int | float] = []
        content: str = re.sub(r"//.*\n", "", s)
        sections: list[str] = re.findall(pattern, content)
        for section in sections:
            if section[-1] == ":":
                if current_p_key:
                    if strict:
                        current_p_value.update({current_s_key: current_s_value})
                    elif len(current_s_value) == 1:
                        current_p_value.update({current_s_key: current_s_value[0]})
                    else:
                        current_p_value.update({current_s_key: current_s_value})
                    result[current_p_key].append(current_p_value)
                current_p_key = section[:-1]
                current_p_value = {}
                current_s_key = ""
                current_s_value = []
            elif section[0] == "." and not util.is_number_and_percent_str(section[1:]):
                if current_s_key:
                    if len(current_s_value) == 1:
                        current_p_value.update({current_s_key: current_s_value[0]})
                    else:
                        current_p_value.update({current_s_key: current_s_value})
                current_s_key = section[1:]
                current_s_value = []
            else:
                if strict:
                    current_s_value.append(section)
                else:
                    if (section[0] == '"' and section[-1] == '"') or (
                        section[0] == "'" and section[-1] == "'"
                    ):
                        current_s_value.append(section[1:-1])
                    elif section.lower() == "true":
                        current_s_value.append(True)
                    elif section.lower() == "false":
                        current_s_value.append(False)
                    elif util.real_int(section):
                        current_s_value.append(int(section))
                    elif util.real_float(section):
                        current_s_value.append(float(section))
                    else:
                        current_s_value.append(darkest.obj(section))
        if current_p_key:
            if strict:
                current_p_value.update({current_s_key: current_s_value})
            elif len(current_s_value) == 1:
                current_p_value.update({current_s_key: current_s_value[0]})
            else:
                current_p_value.update({current_s_key: current_s_value})
            result[current_p_key].append(current_p_value)
        return darkest(result, strict)
