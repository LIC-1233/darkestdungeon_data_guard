from pydantic import Field

from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.trait.trait import trait


class trait_file(BaseModel):
    traits: list[trait] = Field(default=None, title="traits", description="traits")
