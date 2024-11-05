import logging
import re
from collections import defaultdict
from typing import Callable

logger = logging.getLogger()


class util:
    def __init__(self):
        pass

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

    @staticmethod
    def get_data_from_str(
        current_p_key: str, current_s_key: str, datas: list[str]
    ) -> list[str | float | int | bool] | str | float | int | bool:
        result: list[str | float | int | bool] = []
        for data in datas:
            if (data[0] == '"' and data[-1] == '"') or (
                data[0] == "'" and data[-1] == "'"
            ):
                result.append(data[1:-1])
            elif data[-1] == "%":
                precent_count = data.count("%")
                result.append(float(data[:-precent_count]) / 100 * precent_count)
            elif data.lower() == "true":
                result.append(True)
            elif data.lower() == "false":
                result.append(False)
            elif util.real_int(data):
                result.append(int(data))
            elif util.real_float(data):
                result.append(float(data))
            else:
                result.append(data)
        if len(result) == 1:
            return result[0]
        if result == []:
            return 1
        return result


class darkest:
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
                            if isinstance(s_value, str):
                                content += f'"{s_value}" '
                            elif isinstance(s_value, bool):
                                content += f"{s_value} ".lower()
                            elif isinstance(s_value, int):
                                content += f"{s_value} "
                            elif isinstance(s_value, float):  # type: ignore
                                content += f"{s_value} "
                            else:
                                raise TypeError(
                                    f"Unsupported type: {type(s_value)}:{s_value}"
                                )
                    content += "\n"
            return content

    @staticmethod
    def type_check(data: str) -> str | float | int | bool:
        if (data[0] == '"' and data[-1] == '"') or (data[0] == "'" and data[-1] == "'"):
            return data[1:-1]
        elif data[-1] == "%":
            precent_count = data.count("%")
            return float(data[:-precent_count]) / 100 * precent_count
        elif data.lower() == "true":
            return True
        elif data.lower() == "false":
            return False
        elif util.real_int(data):
            return int(data)
        elif util.real_float(data):
            return float(data)
        else:
            return data

    @staticmethod
    def paser_old(s: str, strict: bool = True):
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
        content: str = re.sub(r"//.*(\n)", "\\1", s)
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
                    elif section[-1] == "%":
                        precent_count = section.count("%")
                        current_s_value.append(
                            float(section[:-precent_count]) / 100 * precent_count
                        )
                    elif section.lower() == "true":
                        current_s_value.append(True)
                    elif section.lower() == "false":
                        current_s_value.append(False)
                    elif util.real_int(section):
                        current_s_value.append(int(section))
                    elif util.real_float(section):
                        current_s_value.append(float(section))
                    else:
                        current_s_value.append(section)
        if current_p_key:
            if strict:
                current_p_value.update({current_s_key: current_s_value})
            elif len(current_s_value) == 1:
                current_p_value.update({current_s_key: current_s_value[0]})
            else:
                current_p_value.update({current_s_key: current_s_value})
            result[current_p_key].append(current_p_value)
        return darkest(result, strict)

    @staticmethod
    def paser(
        s: str,
        type_check: Callable[
            [str, str, list[str]],
            list[str | float | int | bool] | str | float | int | bool,
        ] = util.get_data_from_str,
    ):
        result: dict[
            str,
            list[dict[str, list[str | bool | int | float] | str | bool | int | float]],
        ] = defaultdict(list)
        pattern_p = r"(\w+: )"
        pattern_s = r'\.([a-zA-Z_]+)([\d\s"].*?)(?=(?:\.[a-zA-Z_])|\n)'
        pattern_t = r'\s*(".+?")|\s([^\s]+)|([\d\.]+%*)'
        s = re.sub(r"//.*(\n)", "\\1", s)
        p_k_matchs = list(re.finditer(pattern_p, s))
        for current_p_key, current_p_value_start_pos, current_p_value_end_pos in zip(
            [i.groups()[0][:-2] for i in p_k_matchs],
            [i.end() for i in p_k_matchs],
            [i.start() for i in p_k_matchs[1:]] + [len(s)],
            strict=True,
        ):
            current_p_value_str = s[current_p_value_start_pos:current_p_value_end_pos]
            logger.debug([current_p_key, current_p_value_str])
            current_p_value: dict[
                str, list[str | bool | int | float] | str | bool | int | float
            ] = {}
            for current_s_key, current_s_value_str in re.findall(
                pattern_s, current_p_value_str + "\n"
            ):
                logger.debug(current_s_value_str)
                # current_s_value= [type_check(i) for item in re.findall(pattern_t, current_s_value_str) for i in item if i]
                current_s_value_raw = [
                    i
                    for item in re.findall(pattern_t, current_s_value_str)
                    for i in item
                    if i
                ]
                current_s_value = type_check(
                    current_p_key,
                    current_s_key,
                    current_s_value_raw,
                )
                logger.debug(current_s_key, current_s_value)
                current_p_value[current_s_key] = current_s_value
                # current_p_value[current_s_key] = current_s_value[0] if len(current_s_value) == 1 else current_s_value
            result[current_p_key].append(current_p_value)
        return darkest(result, False)

    @staticmethod
    def parser_fast(
        s: str,
        type_check: Callable[
            [str, str, list[str]],
            list[str | float | int | bool] | str | float | int | bool,
        ] = util.get_data_from_str,
    ):
        pattern_p = r"(\w+: )"
        pattern_s = r'\.([a-zA-Z_]+)([\d\s"].*?)(?=(?:\.[a-zA-Z_])|\n)'
        pattern_t = r'\s*(".+?")|\s([^\s]+)|([\d\.]+%*)'
        s = re.sub(r"//.*(\n)", "\\1", s)
        p_k_matchs = list(re.finditer(pattern_p, s))
        for current_p_key, current_p_value_start_pos, current_p_value_end_pos in zip(
            [i.groups()[0][:-2] for i in p_k_matchs],
            [i.end() for i in p_k_matchs],
            [i.start() for i in p_k_matchs[1:]] + [len(s)],
            strict=True,
        ):
            start_line = s[:current_p_value_start_pos].count("\n")
            end_line = s[:current_p_value_end_pos].count("\n")
            current_p_value_str = s[current_p_value_start_pos:current_p_value_end_pos]
            logger.debug([current_p_key, current_p_value_str])
            current_p_value: dict[
                str, list[str | bool | int | float] | str | bool | int | float
            ] = {}
            for current_s_key, current_s_value_str in re.findall(
                pattern_s, current_p_value_str + "\n"
            ):
                logger.debug(current_s_value_str)
                current_s_value_raw = [
                    i
                    for item in re.findall(pattern_t, current_s_value_str)
                    for i in item
                    if i and i != "."
                ]
                try:
                    current_s_value = type_check(
                        current_p_key,
                        current_s_key,
                        current_s_value_raw,
                    )
                except Exception as e:
                    yield ValueError(
                        f"{current_p_key} 解析错误, 位于 {start_line}-{end_line} 行, 错误文本内容: \n\n{current_p_value_str.strip()}\n\n{e}"
                    )
                    continue
                logger.debug(current_s_key, current_s_value)
                current_p_value[current_s_key] = current_s_value
            yield (
                current_p_key,
                current_p_value,
                current_p_value_str,
                start_line,
                end_line,
            )
        yield None
