from typing import Any

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    model_config = {"extra": "forbid"}

    def model_dump_json(self, **kwargs: Any):
        return super().model_dump_json(exclude_defaults=True, **kwargs)
