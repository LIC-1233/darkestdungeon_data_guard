import logging
from pathlib import Path
from types import UnionType
from typing import Literal, Union, get_args, get_origin

from pydantic import BaseModel, ValidationError

from DarkestDungeonClass.dd_game_type.effect.effect_type import effect
from DarkestDungeonClass.dd_game_type.enum.type_enum import (
    int_bool_enum,
)
from DarkestDungeonClass.util import darkest

logger = logging.getLogger()


class data_manager:
    def __init__(self):
        self.effect_id_entries: dict[str, effect] = {}
        self._pk_class: dict[str, type[BaseModel]] = {}
        self._keys_to_type: dict[tuple[str, str], tuple[bool, type]] = {}

        self.init()

    def init(self):
        self._pk_class = {"effect": effect}

        self.init_keys_to_type()

    def init_keys_to_type(self):
        for p_k, cls in self._pk_class.items():
            for s_k, info in cls.model_fields.items():
                is_list = False
                s_ks = [s_k]
                if info.alias:
                    s_ks.append(info.alias)
                if not info.annotation:
                    return None
                annotation = info.annotation
                if get_origin(annotation) is Union:
                    annotation = get_args(annotation)[0]
                    if get_origin(annotation) is list:
                        is_list = True
                        annotation = get_args(annotation)[0]
                if get_origin(annotation) is Literal:
                    annotation = get_args(annotation)[0].__class__
                for s_k in s_ks:
                    self._keys_to_type[(p_k, s_k)] = (is_list, annotation)

    def keys_to_type(self, p_key: str, s_key: str):
        """
        返回一个元组,第一个元素是是否是列表,第二个元素是类型。

        Returns:
                Tuple[bool, type]: 第一个元素是是否是列表，第二个元素是类型。
        """
        return self._keys_to_type.get((p_key, s_key), None)

    def type_check(self, s: str, type: type | UnionType):
        if type is str:
            if (s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'"):
                return s[1:-1]
            else:
                return s
        if type is float:
            precent_count = s.count("%")
            if precent_count > 0:
                return float(s[:-precent_count]) / 100 * precent_count
            return float(s)
        if type is bool:
            if s.lower() == "true":
                return True
            else:
                return False
        if type is int:
            return int(s)
        if type is int_bool_enum:
            return int(s)
        else:
            raise TypeError(f"未知类型: {type}")

    def get_data_from_str(self, p_key: str, s_key: str, data: list[str]):
        if p_key not in self._pk_class:
            raise ValueError(f"未知表名: {p_key}\n\n\n")
        sk_type = self.keys_to_type(p_key, s_key)
        if not sk_type:
            raise ValueError(f"{p_key} 中未知字段: {s_key}\n\n\n")
        is_list, t = sk_type
        try:
            result = [self.type_check(i, t) for i in data if i != ""]
        except Exception as e:
            raise ValueError(
                f"转换错误 表名: {p_key}, 字段: {s_key}, 值: {data}\n\n{e}\n\n\n"
            ) from e
        if not is_list:
            if len(data) == 0:
                result = 1
            elif len(data) > 1:
                pass
                # raise ValueError(f"数据长度 > 1, 数据长度应该为 1, p_k: {p_key}, s_k: {s_key}, s_v: {data}\n\n")
            else:
                result = result[0]
        return result

    def darkest_paser(self, file_path: str | Path):
        s = Path(file_path).read_text(encoding="utf-8", errors="ignore")
        if not s:
            return
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
                if p_k == "effect":
                    e = effect(**p_entery)  # type: ignore
                    self.effect_id_entries[e.name] = e
                else:
                    logger.info(f"未知表名: {p_k}\n\n\n" + "-" * 25)
                    # raise TypeError(f"unexpected p_k: {p_k}\n\n\n")
            except Exception as e:
                if type(e) is ValidationError:
                    error_info = f"在 {e.title} 中共发现 {e.error_count()} 个错误:\n"
                    for index, i in enumerate(e.errors()):
                        error_info += f"第 {index+1} 个错误\n\t错误字段:\t{i['loc'][0]}\n\t错误类型:\t{i['type']}\n\t错误信息:\t{i['msg']}\n\t输入值:\t\t{i["input"]}\n\t输入值类型:\t{type(i["input"]).__name__}"
                    logger.info(
                        f"{file_path} 解析出现错误：\n{p_k} 解析错误, 位于 {start_line}-{end_line} 行, 错误文本内容: \n\n{pasering_str.strip()}\n\n{error_info}\n\n\n"
                        + "-" * 25
                    )
                    # raise Exception(f"{p_k} 解析错误, 位于 {start_line}-{end_line} 行, 错误文本内容: \n\n{pasering_str.strip()}\n\n{error_info}\n\n\n") from e
