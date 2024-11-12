from pydantic import Field

from DarkestDungeonClass.dd_game_type.base import BaseModel


class commonfx_type(BaseModel):
    deathfx: str = Field(
        default="",
        title="Death FX",
        description="Death FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class weapon_type(BaseModel):
    name: str = Field(
        default=None,
        title="武器名",
        description="武器名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    icon: str = Field(
        default=None,
        title="图标",
        description="图标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class armour_type(BaseModel):
    name: str = Field(
        default=None,
        title="防具名",
        description="防具名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    icon: str = Field(
        default=None,
        title="图标",
        description="图标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class combat_skill_type(BaseModel):
    id: str = Field(
        default=None,
        title="战斗技能名",
        description="战斗技能名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    icon: str = Field(
        default=None,
        title="图标",
        description="图标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    anim: str = Field(
        default=None,
        title="动画",
        description="动画",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    fx: str = Field(
        default=None,
        title="FX",
        description="FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    targfx: str = Field(
        default=None,
        title="目标FX",
        description="目标FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    targchestfx: str = Field(
        default=None,
        title="目标FX",
        description="目标FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    targheadfx: str = Field(
        default=None,
        title="目标FX",
        description="目标FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    misstargfx: str = Field(
        default=None,
        title="目标FX",
        description="目标FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    misstargchestfx: str = Field(
        default=None,
        title="目标FX",
        description="目标FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    misstargheadfx: str = Field(
        default=None,
        title="目标FX",
        description="目标FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_display_performer_selection_after_turn: bool = Field(
        default=None,
        title="战斗技能名",
        description="战斗技能名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class combat_move_skill_type(BaseModel):
    id: str = Field(
        default=None,
        title="移动技能名",
        description="移动技能名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    icon: str = Field(
        default=None,
        title="图标",
        description="图标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    anim: str = Field(
        default=None,
        title="动画",
        description="动画",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_display_performer_selection_after_turn: bool = Field(
        default=None,
        title="移动技能名",
        description="移动技能名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class act_out_display_type(BaseModel):
    attack_friendly_anim: str = Field(
        default=None,
        title="攻击友方动画",
        description="攻击友方动画",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    attack_friendly_fx: str = Field(
        default=None,
        title="攻击友方FX",
        description="攻击友方FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    attack_friendly_targchestfx: str = Field(
        default=None,
        title="攻击友方目标FX",
        description="攻击友方目标FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    attack_friendly_sfx: str = Field(
        default=None,
        title="攻击友方SFX",
        description="攻击友方SFX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class rendering_type(BaseModel):
    sort_position_z_rank_override: int = Field(
        default=None,
        title="战斗技能名",
        description="战斗技能名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class hero_art(BaseModel):
    commonfx: commonfx_type = Field(
        default=None,
        title="通用FX",
        description="通用FX",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    weapon: list[weapon_type] = Field(
        default=None,
        title="武器",
        description="武器",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    armour: list[armour_type] = Field(
        default=None,
        title="防具",
        description="防具",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_skill: list[combat_skill_type] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_move_skill: list[combat_move_skill_type] = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    act_out_display: act_out_display_type = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rendering: rendering_type = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
