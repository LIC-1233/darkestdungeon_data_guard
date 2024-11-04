from pydantic import Field

from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.hero import info


class heroes_info(BaseModel):
    id: int = Field(
        default=None,
        title="英雄ID",
        description="英雄ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    resistance: info.resistances = Field(
        default=None,
        title="抗性",
        description="抗性",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: info.crit = Field(
        default=None,
        title="暴击效果",
        description="暴击效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    weapon: list[info.weapon] = Field(
        default=None,
        title="武器",
        description="武器",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    armour: list[info.armour] = Field(
        default=None,
        title="护甲",
        description="护甲",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
