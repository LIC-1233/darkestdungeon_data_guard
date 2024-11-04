from pydantic import BaseModel, Field


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
