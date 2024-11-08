from typing import Any

from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    model_config = {
        "extra": "forbid",
        "populate_by_name": True,
        "arbitrary_types_allowed": True,
    }

    def model_dump_json(self, **kwargs: Any):
        return super().model_dump_json(exclude_defaults=True, **kwargs)

    def model_dump(self, **kwargs: Any):
        return super().model_dump(exclude_defaults=True, **kwargs)