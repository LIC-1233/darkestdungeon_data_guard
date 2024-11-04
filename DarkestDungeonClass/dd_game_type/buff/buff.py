from pydantic import Field

from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.enum.type_enum import buff_stat_types_enum


class buff_stat_types(BaseModel):
    hp_heal_amount: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_stat_multiply: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_stat_add: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    resistance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    poison_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    bleed_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dmg_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dmg_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_heal_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_heal_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    party_surprise_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    monsters_surprise_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ambush_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    scouting_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    starving_damage_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    upgrade_discount: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    debuff_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    resolve_check_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stun_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    move_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    remove_negative_quirk_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    food_consumption_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    resolve_xp_bonus_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    activity_side_effect_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    vampire_evolution_duration: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    quirk_evolution_death_immune: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    disable_combat_skill_attribute: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guard_blocked: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tag_blocked: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_protection: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_stealth: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit_received_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tag: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stealth: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_heal: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffle_dot: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guarded: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    status: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    vampire: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torch_increase_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torch_decrease_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torchlight_burn_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_on_miss: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_from_idle_in_town: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shard_reward_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shard_consume_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_reflect_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_duration_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_duration_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_amount_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_bleed_amount_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_duration_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_duration_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_amount_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_dot_poison_amount_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_duration_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_duration_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_amount_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress_dot_amount_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_duration_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_duration_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_amount_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    hp_heal_dot_amount_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffle_dot_duration_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffle_dot_duration_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guard_duration_received_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guard_duration_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_bleed_received_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_poison_received_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_bleed_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_poison_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    random_target_friendly_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    random_target_attack_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    transfer_debuff_from_attacker_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    transfer_buff_from_attacker_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    quirk_tag_evolution_duration: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    deathblow_chance: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    heartattack_stress_heal_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    ignore_guard: int = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_duration_percent: float = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_duration_percent: float = Field(
        default=None,
    )


class rule_data_type(BaseModel):
    value: float = Field(
        alias="float",
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    string: str = Field(
        default=None,
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class buff(BaseModel):
    id: str = Field(
        default=None,
        title="ID",
        description="ID",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stat_type: buff_stat_types_enum = Field(
        default=None,
        title="状态类型",
        description="状态类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stat_sub_type: str = Field(
        default=None,
        title="状态子类型",
        description="状态子类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    amount: float = Field(
        default=None,
        title="数量",
        description="数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    duration_type: str = Field(
        default=None,
        title="持续类型",
        description="持续类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    duration: int = Field(
        default=None,
        title="持续时间",
        description="持续时间",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    remove_if_not_active: bool = Field(
        default=None,
        title="不激活时删除",
        description="不激活时删除",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    remove_on_battle_complete: bool = Field(
        default=None,
        title="战斗结束时删除",
        description="战斗结束时删除",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rule_type: str = Field(
        default=None,
        title="规则类型",
        description="规则类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_false_rule: bool = Field(
        default=None,
        title="是否为反选",
        description="是否为反选",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rule_data: rule_data_type = Field(
        default=None,
        title="规则数据",
        description="规则数据",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    is_clear_debuff_valid: bool = Field(
        default=None,
        title="是否为清除Debuff",
        description="是否为清除Debuff",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    has_description: bool = Field(
        default=None,
        title="是否有描述",
        description="是否有描述",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    fx: str = Field(
        default=None,
        title="特效",
        description="特效",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )


class buff_table(BaseModel):
    buffs: list[buff] = Field(
        default=None,
        title="buff列表",
        description="buff列表",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
