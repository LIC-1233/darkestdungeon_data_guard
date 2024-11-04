from pydantic import BaseModel, Field, ValidationError

from DarkestDungeonClass.dd_game_type.effect import effect_type


class resistances(BaseModel):
    stun: float = Field(
        default=None,
        title="眩晕抗性",
        description="眩晕抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    poison: float = Field(
        default=None,
        title="中毒抗性",
        description="中毒抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    bleed: float = Field(
        default=None,
        title="流血抗性",
        description="流血抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    disease: float = Field(
        default=None,
        title="疾病抗性",
        description="疾病抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    move: float = Field(
        default=None,
        title="移动抗性",
        description="移动抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    debuff: float = Field(
        default=None,
        title="减益抗性",
        description="减益抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    death_blow: float = Field(
        default=None,
        title="死亡抗性",
        description="死亡抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    trap: float = Field(
        default=None,
        title="陷阱抗性",
        description="陷阱抗性",
        examples=[0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class crit(BaseModel):
    effects: list[effect_type.effect] = Field(
        default=None,
        title="暴击效果",
        description="暴击效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class weapon(BaseModel):
    name: str = Field(
        default=None,
        title="武器名",
        description="武器名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    atk: float = Field(
        default=None,
        title="武器命中",
        description="武器命中",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dmg: tuple[int, int] = Field(
        default=None,
        title="武器伤害",
        description="武器伤害",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: float = Field(
        default=None,
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    spd: int = Field(
        default=None,
        title="武器速度",
        description="武器速度",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defence: float = Field(
        default=None,
        alias="def",
        title="闪避",
        description="闪避",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    prot: float = Field(
        default=None,
        title="减伤",
        description="减伤",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp: int = Field(
        default=None,
        title="生命",
        description="生命",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    upgradeRequirementCode: int = Field(
        default=None,
        title="升级需求",
        description="升级需求",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class armour(BaseModel):
    name: str = Field(
        default=None,
        title="武器名",
        description="武器名",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    atk: float = Field(
        default=None,
        title="武器命中",
        description="武器命中",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dmg: tuple[int, int] = Field(
        default=None,
        title="武器伤害",
        description="武器伤害",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: float = Field(
        default=None,
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    spd: int = Field(
        default=None,
        title="武器速度",
        description="武器速度",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defence: float = Field(
        default=None,
        alias="def",
        title="闪避",
        description="闪避",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    prot: float = Field(
        default=None,
        title="减伤",
        description="减伤",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp: int = Field(
        default=None,
        title="生命",
        description="生命",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    upgradeRequirementCode: int = Field(
        default=None,
        title="升级需求",
        description="升级需求",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class combat_skill(BaseModel):
    class Config:
        extra = "allow"  # 忽略额外字段

    def __post_init__(self):
        # 获取模型中定义的字段名

        if self.__pydantic_extra__:
            defined_fields = set(self.model_fields.keys())

            # 提取特定名称的额外字段
            allowed_extra_fields = {
                k for k in self.__pydantic_extra__.keys() if k.endswith("_effects")
            }  # 这里定义允许的额外字段

            # 如果有不允许的额外字段，抛出 ValidationError
            disallowed_extra = {
                k
                for k in self.__pydantic_extra__.keys()
                if k not in allowed_extra_fields | defined_fields
            }
            if disallowed_extra:
                raise ValidationError(f"Disallowed extra fields: {disallowed_extra}")

    id: str = Field(
        default=None,
        title="技能id",
        description="技能id",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    level: int = Field(
        default=None,
        title="技能等级",
        description="技能等级",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    type: str = Field(
        default=None,
        title="技能类型",
        description="技能类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    atk: float = Field(
        default=None,
        title="武器命中",
        description="武器命中",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dmg: float = Field(
        default=None,
        title="武器伤害增加",
        description="武器伤害增加",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit: float = Field(
        default=None,
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defence: float = Field(
        default=None,
        alias="def",
        title="武器暴击率",
        description="武器暴击率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    move: tuple[int, int] = Field(
        default=None,
        title="可移动距离[前,后]",
        description="可移动距离[前,后]",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    starting_cooldown: int = Field(
        default=None,
        title="初始冷却时间",
        description="初始冷却时间",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    per_battle_limit: int = Field(
        default=None,
        title="每场战斗限制",
        description="每场战斗限制",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    per_turn_limit: int = Field(
        default=None,
        title="每回合限制",
        description="每回合限制",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_continue_turn: bool = Field(
        default=None,
        title="是否连续回合",
        description="是否连续回合",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    launch: str = Field(
        default=None,
        title="技能释放位置",
        description="技能释放位置",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    target: str = Field(
        default=None,
        title="技能目标位置",
        description="技能目标位置",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    self_target_valid: bool = Field(
        default=None,
        title="是否自身目标",
        description="是否自身目标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_targets_chance: float = Field(
        default=None,
        title="额外目标概率",
        description="额外目标概率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    extra_targets_count: int = Field(
        default=None,
        title="额外目标数量",
        description="额外目标数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_crit_valid: bool = Field(
        default=None,
        title="是否暴击",
        description="是否暴击",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    effect: list[effect_type.effect] = Field(
        default=None,
        title="技能效果",
        description="技能效果",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    valid_modes: list[str] = Field(
        default=None,
        title="有效模式",
        description="有效模式",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_stealth: bool = Field(
        default=None,
        title="是否无视隐身",
        description="是否无视隐身",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_guard: bool = Field(
        default=None,
        title="是否无视防御",
        description="是否无视防御",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_miss: bool = Field(
        default=None,
        title="是否允许闪避",
        description="是否允许闪避",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_be_riposted: bool = Field(
        default=None,
        title="是否允许反击",
        description="是否允许反击",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_protection: bool = Field(
        default=None,
        title="是否无视防御",
        description="是否无视防御",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    required_performer_hp_range: tuple[int, int] = Field(
        default=None,
        title="执行者生命值范围",
        description="执行者生命值范围",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rank_damage_modifiers: float = Field(
        default=None,
        title="等级伤害修正",
        description="等级伤害修正",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    heal: bool = Field(
        default=None,
        title="是否治疗",
        description="是否治疗",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_crit_heal: bool = Field(
        default=None,
        title="是否允许暴击治疗",
        description="是否允许暴击治疗",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    generation_guaranteed: bool = Field(
        default=None,
        title="是否强制生成",
        description="是否强制生成",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_user_selected_targets: bool = Field(
        default=None,
        title="是否用户选择目标",
        description="是否用户选择目标",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_knowledgeable: bool = Field(
        default=None,
        title="是否擅长",
        description="是否擅长",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_monster_rerank_valid_on_attack: bool = Field(
        default=None,
        title="是否攻击时重排怪物",
        description="是否攻击时重排怪物",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_monster_rerank_valid_on_friendly_presentation_end: bool = Field(
        default=None,
        title="是否友方回合结束时重排怪物",
        description="是否友方回合结束时重排怪物",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_monster_rerank_valid_on_friendly_post_result: bool = Field(
        default=None,
        title="是否友方回合结束后重排怪物",
        description="是否友方回合结束后重排怪物",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_stall_invalidating: bool = Field(
        default=None,
        title="是否无效",
        description="是否无效",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    refresh_after_each_wave: bool = Field(
        default=None,
        title="是否刷新每波",
        description="是否刷新每波",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_heal_base_class_ids: list[int] = Field(
        default=None,
        title="伤害治疗基类ID",
        description="伤害治疗基类ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_deathsdoor: bool = Field(
        default=None,
        title="是否忽略死亡门",
        description="是否忽略死亡门",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
