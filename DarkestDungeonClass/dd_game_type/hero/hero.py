from pydantic import Field

from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.hero.art import hero_art
from DarkestDungeonClass.dd_game_type.hero.info import hero_info


class hero(BaseModel):
    art: hero_art = Field(
        default=None,
        title="英雄艺术",
        description="英雄艺术",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    info: hero_info = Field(
        default=None,
        title="英雄信息",
        description="英雄信息",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )