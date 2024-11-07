import logging
import re
from collections import defaultdict
from pathlib import Path
from types import UnionType
from typing import Callable, Literal, get_args, get_origin

from pydantic import BaseModel, ValidationError

from DarkestDungeonClass.dd_game_type.effect.effect import effect
from DarkestDungeonClass.dd_game_type.enum.type_enum import (
    int_bool_enum,
)
from DarkestDungeonClass.dd_game_type.file.effect import effect_file
from DarkestDungeonClass.dd_game_type.file.hero_info import heroes_info_file

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
        strict: bool = False,
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
            list[str | float | int | bool]
            | str
            | float
            | int
            | bool
            | tuple[str | float | int | bool, ...],
        ] = util.get_data_from_str,
    ):
        pattern_p = r"(\w+: )"
        pattern_s = r'\.([a-zA-Z_]+)([\d\s"].*?)(?=(?:\.[a-zA-Z_])|\n|$)'
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
                str,
                list[str | bool | int | float]
                | str
                | bool
                | int
                | float
                | tuple[str | float | int | bool, ...],
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


class file_parser:
    def __init__(self, file_type: Literal["hero_info", "effect"]):
        self.file_type = file_type

        self.init()

    def init(self) -> None:
        self.file_pk_type = {"hero_info": heroes_info_file, "effect": effect_file}
        self.effect_id_entries: dict[str, list[effect]] = defaultdict(list)
        self.pk_id_entries: dict[str, list[BaseModel]] = defaultdict(list)
        self._keys_to_type: dict[tuple[str, str], type] = {}
        self.pk_extra: dict[str, bool] = defaultdict(bool)
        self._pk_class: dict[str, type[BaseModel]] = {}
        self.init_pk_class()
        self.init_keys_to_type()

    def init_pk_class(self):
        for p_k, cls in self.file_pk_type[self.file_type].__annotations__.items():
            if get_origin(cls) is list:
                self._pk_class[p_k] = get_args(cls)[0]
            else:
                self._pk_class[p_k] = cls

    def init_keys_to_type(self):
        for p_k, cls in self._pk_class.items():
            if get_origin(cls) is list:
                cls = get_args(cls)[0]
            for s_k, info in cls.model_fields.items():
                s_ks = [s_k]
                if info.alias:
                    s_ks.append(info.alias)
                if not info.annotation:
                    return None
                annotation = info.annotation
                for s_k in s_ks:
                    self._keys_to_type[(p_k, s_k)] = annotation
            self.pk_extra[p_k] = cls.model_config.get("extra", "ignore") == "allow"

    def keys_to_type(self, p_key: str, s_key: str):
        """
        返回一个元组,第一个元素是是否是列表,第二个元素是类型。

        Returns:
                type: 元素是类型。
        """
        return self._keys_to_type.get((p_key, s_key), None)

    def type_check2(
        self, data: list[str], type: type | UnionType
    ) -> (
        str
        | float
        | int
        | bool
        | list[str | float | int | bool]
        | tuple[str | float | int | bool, ...]
    ):
        if get_origin(type) is list:
            return [self.type_check(i, get_args(type)[0]) for i in data if i != ""]
        elif get_origin(type) is tuple:
            sub_types = get_args(type)
            if len(sub_types) != len(data):
                raise ValueError(f"tuple类型错误：元素长度不匹配，{data}")
            return tuple(
                [
                    self.type_check(data[index], sub_types[index])
                    for index in range(len(sub_types))
                ]
            )
        else:
            if len(data) > 1:
                logger.error(f"类型错误：元素长度大于 1，使用第一个元素继续，{data}")
                return self.type_check(data[0], type)
            elif len(data) == 0:
                return self.type_check("", type)
            return self.type_check(data[0], type)

    def type_check(self, s: str, Vtype: type | UnionType) -> str | float | int | bool:
        if Vtype is Literal[1, 0]:
            if s == "":
                return 0
        if Vtype is str:
            if s == "":
                return s
            if (s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'"):
                return s[1:-1]
            else:
                return s
        if Vtype is float:
            precent_count = s.count("%")
            if precent_count > 0:
                return float(s[:-precent_count]) / 100 * precent_count
            return float(s)
        if Vtype is bool:
            if s == "":
                return True
            if s.lower() == "true":
                return True
            else:
                return False
        if Vtype is int:
            return int(s)
        if Vtype is int_bool_enum:
            return int(s)
        if get_origin(Vtype) is Literal:
            for i in get_args(Vtype):
                try:
                    if self.type_check(s, type(i)):  # type: ignore
                        return i
                except Exception:
                    pass
            raise TypeError(f"Literal未知类型: {Vtype}")
        if get_origin(Vtype) is UnionType:
            for i in get_args(Vtype):
                try:
                    if v := self.type_check(s, i):  # type: ignore
                        return v
                except Exception:
                    pass
            raise TypeError(f"Literal未知类型: {Vtype}")
        else:
            raise TypeError(f"未知类型: {Vtype}")

    def get_data_from_str(
        self, p_key: str, s_key: str, data: list[str]
    ) -> (
        list[str | float | int | bool]
        | str
        | float
        | int
        | bool
        | tuple[str | float | int | bool, ...]
    ):
        if p_key not in self._pk_class:
            raise ValueError(f"未知表名: {p_key}\n\n\n")
        sk_type = self.keys_to_type(p_key, s_key)
        if not sk_type:
            if self.pk_extra[p_key]:
                sk_type = list[str]
            else:
                raise ValueError(f"{p_key} 中未知字段: {s_key}\n\n\n")

        svalue_type = sk_type
        try:
            result: (
                str
                | float
                | int
                | bool
                | list[str | float | int | bool]
                | tuple[str | float | int | bool, ...]
            ) = self.type_check2(data, svalue_type)
        except Exception as e:
            raise ValueError(
                f"转换错误 表名: {p_key}, 字段: {s_key}, 值: {data}\n\n{e}\n\n\n"
            ) from e
        return result

    def darkest_paser(self, file_path: str | Path):
        self.init()
        s = Path(file_path).read_text(encoding="utf-8", errors="ignore")
        if not s:
            return self.file_pk_type[self.file_type]()
        for darkest_parser_result in darkest.parser_fast(s, self.get_data_from_str):
            if not darkest_parser_result:
                continue
            if isinstance(darkest_parser_result, Exception):
                logger.info(
                    f"{file_path} 解析出现错误：\n{darkest_parser_result}" + "-" * 25
                )
                continue
            p_k, p_entery, pasering_str, start_line, end_line = darkest_parser_result
            try:
                if p_k in self._pk_class.keys():
                    e = self._pk_class[p_k](**p_entery)  # type: ignore
                    self.pk_id_entries[p_k].append(e)
                else:
                    logger.info(f"未知表名: {p_k}\n\n\n" + "-" * 25)
            except Exception as e:
                if type(e) is ValidationError:
                    error_info = f"在 {e.title} 中共发现 {e.error_count()} 个错误:\n"
                    for index, i in enumerate(e.errors()):
                        error_info += f"第 {index+1} 个错误\n\t错误字段:\t{i['loc'][0]}\n\t错误类型:\t{i['type']}\n\t错误信息:\t{i['msg']}\n\t输入值:\t\t{i["input"]}\n\t输入值类型:\t{type(i["input"]).__name__}\n"
                    logger.info(
                        f"{file_path} 解析出现错误：\n{p_k} 解析错误, 位于 {start_line}-{end_line} 行, 错误文本内容: \n\n{pasering_str.strip()}\n\n{error_info}\n\n\n"
                        + "-" * 25
                    )
                    # raise Exception(f"{p_k} 解析错误, 位于 {start_line}-{end_line} 行, 错误文本内容: \n\n{pasering_str.strip()}\n\n{error_info}\n\n\n") from e
        return self.file_pk_type[self.file_type](**self.pk_id_entries)  # type: ignore
