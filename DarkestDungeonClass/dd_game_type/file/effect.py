from pydantic import Field

from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.effect.effect import effect as effect_type


class effect_file(BaseModel):
    effect: list[effect_type] = Field(
        default=None,
    )
