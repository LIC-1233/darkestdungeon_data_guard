import logging
from pathlib import Path
from types import UnionType
from typing import Literal, Optional, Union, get_args, get_origin

from pydantic import BaseModel, Field, ValidationError

from DarkestDungeonClass.type_enum import (
    buff_duration_type_enum,
    buff_sources_enum,
    buff_stat_types_enum,
    curio_result_type_enum,
    damage_source_type_enum,
    damage_type_enum,
    int_bool_enum,
    keyState_enum,
    source_heal_type_enum,
    target_enum,
)
from DarkestDungeonClass.util import darkest

logger = logging.getLogger()


class buff_stat_types(BaseModel):
    hp_heal_amount: int = Field(
        default=None,
    )
    hp_heal_percent: float = Field(
        default=None,
    )
    hp_heal_received_percent: float = Field(
        default=None,
    )
    combat_stat_multiply: float = Field(
        default=None,
    )
    combat_stat_add: float = Field(
        default=None,
    )
    resistance: float = Field(
        default=None,
    )
    poison_chance: float = Field(
        default=None,
    )
    bleed_chance: float = Field(
        default=None,
    )
    stress_dmg_percent: float = Field(
        default=None,
    )
    stress_dmg_received_percent: float = Field(
        default=None,
    )
    stress_heal_percent: float = Field(
        default=None,
    )
    stress_heal_received_percent: float = Field(
        default=None,
    )
    party_surprise_chance: float = Field(
        default=None,
    )
    monsters_surprise_chance: float = Field(
        default=None,
    )
    ambush_chance: float = Field(
        default=None,
    )
    scouting_chance: float = Field(
        default=None,
    )
    starving_damage_percent: float = Field(
        default=None,
    )
    upgrade_discount: int = Field(
        default=None,
    )
    damage_received_percent: float = Field(
        default=None,
    )
    debuff_chance: float = Field(
        default=None,
    )
    resolve_check_percent: float = Field(
        default=None,
    )
    stun_chance: float = Field(
        default=None,
    )
    move_chance: float = Field(
        default=None,
    )
    remove_negative_quirk_chance: float = Field(
        default=None,
    )
    food_consumption_percent: float = Field(
        default=None,
    )
    resolve_xp_bonus_percent: float = Field(
        default=None,
    )
    activity_side_effect_chance: float = Field(
        default=None,
    )
    vampire_evolution_duration: int = Field(
        default=None,
    )
    quirk_evolution_death_immune: int = Field(
        default=None,
    )
    disable_combat_skill_attribute: float = Field(
        default=None,
    )
    guard_blocked: int = Field(
        default=None,
    )
    tag_blocked: int = Field(
        default=None,
    )
    ignore_protection: float = Field(
        default=None,
    )
    ignore_stealth: int = Field(
        default=None,
    )
    crit_received_chance: float = Field(
        default=None,
    )
    riposte: int = Field(
        default=None,
    )
    tag: int = Field(
        default=None,
    )
    stealth: int = Field(
        default=None,
    )
    hp_dot_bleed: int = Field(
        default=None,
    )
    hp_dot_poison: int = Field(
        default=None,
    )
    hp_dot_heal: int = Field(
        default=None,
    )
    stress_dot: int = Field(
        default=None,
    )
    shuffle_dot: int = Field(
        default=None,
    )
    guarded: float = Field(
        default=None,
    )
    status: float = Field(
        default=None,
    )
    vampire: float = Field(
        default=None,
    )
    torch_increase_percent: float = Field(
        default=None,
    )
    torch_decrease_percent: float = Field(
        default=None,
    )
    torchlight_burn_percent: float = Field(
        default=None,
    )
    stress_on_miss: int = Field(
        default=None,
    )
    stress_from_idle_in_town: int = Field(
        default=None,
    )
    shard_reward_percent: float = Field(
        default=None,
    )
    shard_consume_percent: float = Field(
        default=None,
    )
    damage_reflect_percent: float = Field(
        default=None,
    )
    hp_dot_bleed_duration_received_percent: float = Field(
        default=None,
    )
    hp_dot_bleed_duration_percent: float = Field(
        default=None,
    )
    hp_dot_bleed_amount_received_percent: float = Field(
        default=None,
    )
    hp_dot_bleed_amount_percent: float = Field(
        default=None,
    )
    hp_dot_poison_duration_received_percent: float = Field(
        default=None,
    )
    hp_dot_poison_duration_percent: float = Field(
        default=None,
    )
    hp_dot_poison_amount_received_percent: float = Field(
        default=None,
    )
    hp_dot_poison_amount_percent: float = Field(
        default=None,
    )
    stress_dot_duration_received_percent: float = Field(
        default=None,
    )
    stress_dot_duration_percent: float = Field(
        default=None,
    )
    stress_dot_amount_received_percent: float = Field(
        default=None,
    )
    stress_dot_amount_percent: float = Field(
        default=None,
    )
    hp_heal_dot_duration_received_percent: float = Field(
        default=None,
    )
    hp_heal_dot_duration_percent: float = Field(
        default=None,
    )
    hp_heal_dot_amount_received_percent: float = Field(
        default=None,
    )
    hp_heal_dot_amount_percent: float = Field(
        default=None,
    )
    shuffle_dot_duration_received_percent: float = Field(
        default=None,
    )
    shuffle_dot_duration_percent: float = Field(
        default=None,
    )
    guard_duration_received_percent: float = Field(
        default=None,
    )
    guard_duration_percent: float = Field(
        default=None,
    )
    cure_bleed_received_chance: float = Field(
        default=None,
    )
    cure_poison_received_chance: float = Field(
        default=None,
    )
    cure_bleed_chance: float = Field(
        default=None,
    )
    cure_poison_chance: float = Field(
        default=None,
    )
    random_target_friendly_chance: float = Field(
        default=None,
    )
    random_target_attack_chance: float = Field(
        default=None,
    )
    transfer_debuff_from_attacker_chance: float = Field(
        default=None,
    )
    transfer_buff_from_attacker_chance: float = Field(
        default=None,
    )
    quirk_tag_evolution_duration: int = Field(
        default=None,
    )
    deathblow_chance: float = Field(
        default=None,
    )
    heartattack_stress_heal_percent: float = Field(
        default=None,
    )
    ignore_guard: int = Field(
        default=None,
    )
    buff_duration_percent: float = Field(
        default=None,
    )
    riposte_duration_percent: float = Field(
        default=None,
    )


class effect(BaseModel):
    name: str = Field(
        default=None,
        title="effect id",
        description="effect的唯一标识符",
        examples=["Manacles Stun 1"],
    )
    target: Optional[target_enum] = Field(
        default=None,
        title="目标",
        description="effect的目标",
        examples=[
            "performer",
            "performer_group",
            "performer_group_other",
            "target",
            "target_group",
            "target_group_other",
            "target_enemy_group",
            "global",
        ],
    )
    curio_result_type: Optional[curio_result_type_enum] = Field(
        default=None,
        title="Curio结果类型",
        description="Curio的结果类型",
        examples=["positive", "negative", "neutral", "none"],
    )
    chance: Optional[float] = Field(
        default=None,
        title="施加概率",
        description="effect的施加概率",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    on_hit: Optional[bool] = Field(
        default=None,
        title="命中触发",
        description="effect是否命中触发",
        examples=[True, False],
    )
    on_miss: Optional[bool] = Field(
        default=None,
        title="未命中触发",
        description="effect是否未命中触发",
        examples=[True, False],
    )
    queue: Optional[bool] = Field(
        default=None,
        title="effect是否最后结算",
        description="effect是否最后结算",
        examples=[True, False],
    )
    dotBleed: Optional[int] = Field(
        default=None,
        title="流血量",
        description="effect的流血量",
        examples=[1, 2, 3],
    )
    dotPoison: Optional[int] = Field(
        default=None,
        title="腐蚀量",
        description="effect的腐蚀量",
        examples=[1, 2, 3],
    )
    dotStress: Optional[int] = Field(
        default=None,
        title="持续加压量",
        description="effect的持续加压量",
        examples=[1, 2, 3],
    )
    stress: Optional[int] = Field(
        default=None,
        title="加压量",
        description="effect的加压量",
        examples=[1, 2, 3],
    )
    healstress: Optional[int] = Field(
        default=None,
        title="减压量",
        description="effect的减压量",
        examples=[1, 2, 3],
    )
    combat_stat_buff: Optional[int_bool_enum] = Field(
        default=None,
        title="修改属性",
        description="effect能否修改属性",
        examples=[True, False],
    )
    damage_low_multiply: Optional[float] = Field(
        default=None,
        title="伤害下限叠乘",
        description="effect的伤害下限叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    damage_low_add: Optional[int] = Field(
        default=None,
        title="伤害下限叠加",
        description="effect的伤害下限叠加",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    damage_high_multiply: Optional[float] = Field(
        default=None,
        title="伤害上限叠乘",
        description="effect的伤害上限叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    damage_high_add: Optional[int] = Field(
        default=None,
        title="伤害上限叠加",
        description="effect的伤害上限叠加",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    max_hp_multiply: Optional[float] = Field(
        default=None,
        title="最大hp叠乘",
        description="effect的最大hp叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    max_hp_add: Optional[int] = Field(
        default=None,
        title="最大hp叠加",
        description="effect的最大hp叠加",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    attack_rating_multiply: Optional[float] = Field(
        default=None,
        title="精准叠乘",
        description="effect的精准叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    attack_rating_add: Optional[float] = Field(
        default=None,
        title="精准叠加",
        description="effect的精准叠加，注意这里是百分比",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    crit_chance_multiply: Optional[float] = Field(
        default=None,
        title="暴击率叠乘",
        description="effect的暴击率叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    crit_chance_add: Optional[float] = Field(
        default=None,
        title="暴击率叠加",
        description="effect的暴击率叠加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    defense_rating_multiply: Optional[float] = Field(
        default=None,
        title="闪避叠乘",
        description="effect的闪避叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    defense_rating_add: Optional[float] = Field(
        default=None,
        title="闪避叠加",
        description="effect的闪避叠加，注意这里是百分比",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    protection_rating_multiply: Optional[float] = Field(
        default=None,
        title="护甲叠乘",
        description="effect的护甲叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    protection_rating_add: Optional[float] = Field(
        default=None,
        title="护甲叠加",
        description="effect的护甲叠加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    speed_rating_multiply: Optional[float] = Field(
        default=None,
        title="速度叠乘",
        description="effect的速度叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    speed_rating_add: Optional[float] = Field(
        default=None,
        title="速度叠加",
        description="effect的速度叠加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    buff_ids: Optional[list[str]] = Field(
        default=None,
        title="施加的buff ids",
        description="buff的唯一标识符列表",
        examples=["Manacles Stun 1", "Manacles Stun 2"],
    )
    duration: Optional[int] = Field(
        default=None,
        title="持续时间",
        description="effect的持续时间",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    dotHpHeal: Optional[int] = Field(
        default=None,
        title="持续治愈量",
        description="effect的持续治愈量",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    heal: Optional[int] = Field(
        default=None,
        title="治愈量",
        description="effect的治愈量",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    heal_percent: Optional[float] = Field(
        default=None,
        title="治愈百分比",
        description="effect的治愈百分比",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    can_crit_heal: Optional[bool] = Field(
        default=None,
        title="治愈是否可暴击",
        description="effect的治愈是否可以暴击",
        examples=[True, False],
    )
    cure: Optional[int_bool_enum] = Field(
        default=None,
        title="治愈腐蚀流血",
        description="effect是否可以治愈目标腐蚀流血",
        examples=[1, 0],
    )
    cure_bleed: Optional[int_bool_enum] = Field(
        default=None,
        title="治愈流血",
        description="effect是否可以治愈目标流血",
        examples=[1, 0],
    )
    cure_poison: Optional[int_bool_enum] = Field(
        default=None,
        title="治愈腐蚀",
        description="effect是否可以治愈目标腐蚀",
        examples=[1, 0],
    )
    clearDotStress: Optional[int_bool_enum] = Field(
        default=None,
        title="清除惊恐",
        description="effect是否可以清除目标惊恐",
        examples=[1, 0],
    )
    tag: Optional[int_bool_enum] = Field(
        default=None,
        title="标记",
        description="effect是否可以标记目标",
        examples=[1, 0],
    )
    untag: Optional[int_bool_enum] = Field(
        default=None,
        title="清除标记",
        description="effect是否可以清除目标标记",
        examples=[1, 0],
    )
    stun: Optional[int_bool_enum] = Field(
        default=None,
        title="眩晕",
        description="effect是否可以眩晕目标",
        examples=[1, 0],
    )
    unstun: Optional[int_bool_enum] = Field(
        default=None,
        title="清除眩晕",
        description="effect是否可以清除目标眩晕",
        examples=[1, 0],
    )
    keyStatus: Optional[keyState_enum] = Field(
        default=None,
        title="目标是否对应状态",
        description="effect的目标有对应状态，则effect生效",
        examples=[
            "tagged",
            "poisoned",
            "bleeding",
            "stunned",
            "dazed",
            "virtued",
            "afflicted",
            "transformed",
        ],
    )
    riposte: Optional[int_bool_enum] = Field(
        default=None,
        title="反击",
        description="是否激活目标反击",
        examples=[1, 0],
    )
    riposte_on_miss_chance_add: Optional[float] = Field(
        default=None,
        title="反击时闪避概率增加",
        description="反击时闪避概率增加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    riposte_on_hit_chance_add: Optional[float] = Field(
        default=None,
        title="反击时命中概率增加",
        description="反击时命中概率增加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    riposte_on_miss_chance_multiply: Optional[float] = Field(
        default=None,
        title="反击时闪避概率叠乘",
        description="反击时闪避概率叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    riposte_on_hit_chance_multiply: Optional[float] = Field(
        default=None,
        title="反击时命中概率叠乘",
        description="反击时命中概率叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    riposte_effect: Optional[list[str]] = Field(
        default=None,
        title="反击效果",
        description="反击效果",
        examples=[
            "Manacles Stun 1",
            "Manacles Stun 2",
            "Manacles Stun 3",
            "Manacles Stun 4",
            "Manacles Stun 5",
            "Manacles Stun 6",
            "Manacles Stun 7",
            "Manacles Stun 8",
            "Manacles Stun 9",
            "Manacles Stun 10",
        ],
    )
    clear_riposte: Optional[int_bool_enum] = Field(
        default=None,
        title="清除反击",
        description="effect是否可以清除目标反击",
        examples=[1, 0],
    )
    guard: Optional[int_bool_enum] = Field(
        default=None,
        title="守护目标",
        description="是否可以守护目标",
        examples=[1, 0],
    )
    clearguarding: Optional[int_bool_enum] = Field(
        default=None,
        title="清除守护",
        description="effect是否可以取消目标守护的状态",
        examples=[1, 0],
    )
    clearguarded: Optional[int_bool_enum] = Field(
        default=None,
        title="清除守护",
        description="effect是否可以清除目标被守护的状态",
        examples=[1, 0],
    )
    torch_decrease: Optional[int] = Field(
        default=None,
        title="减少火把亮度",
        description="减少火把亮度",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    torch_increase: Optional[int] = Field(
        default=None,
        title="增加火把亮度",
        description="增加火把亮度",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    )
    item: Optional[int_bool_enum] = Field(
        default=None,
        title="来自物品？",
        description="是否来自物品",
        examples=[1, 0],
    )
    curio: Optional[int_bool_enum] = Field(
        default=None,
        title="来自饰品？",
        description="是否来自饰品",
        examples=[1, 0],
    )
    dotShuffle: Optional[int_bool_enum] = Field(
        default=None,
        title="持续乱位",
        description="是否持续乱位",
        examples=[1, 0],
    )
    push: Optional[int] = Field(
        default=None,
        title="推后目标",
        description="推后目标",
        examples=[1, 2, 3],
    )
    pull: Optional[int] = Field(
        default=None,
        title="拉前目标",
        description="拉前目标",
        examples=[1, 2, 3],
    )
    shuffletarget: Optional[int_bool_enum] = Field(
        default=None,
        title="乱位目标",
        description="是否可以乱位目标",
        examples=[1, 0],
    )
    shuffleparty: Optional[int_bool_enum] = Field(
        default=None,
        title="乱位整队",
        description="是否可以乱位目标整队",
        examples=[1, 0],
    )
    instant_shuffle: Optional[int_bool_enum] = Field(
        default=None,
        title="立即乱位",
        description="是否可以立即乱位",
        examples=[1, 0],
    )
    buff_amount: Optional[float] = Field(
        default=None,
        title="buff值",
        description="施加buff的值比如治疗的值",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    )
    buff_type: Optional[str] = Field(
        default=None,
        title="buff类型",
        description="施加buff的类型",
        examples=[
            "hp_heal_received_percent",
            "torchlight_burn_percent",
        ],
    )
    buff_sub_type: Optional[str] = Field(
        default=None,
        title="buff子类型",
        description="施加buff的子类型",
        examples=[
            "hp_heal_amount",
            "hp_heal_percent",
            "hp_heal_received_percent",
            "riposte_duration_percent	",
        ],
    )
    buff_duration_type: Optional[buff_duration_type_enum] = Field(
        default=None,
        alias="duration_type",
        title="buff持续时间类型",
        description="施加buff的持续时间类型",
        examples=[
            "round",
            "combat_end",
            "quest_end",
            "quest_complete",
            "quest_not_complete",
            "activity_end",
            "idle_start_town_visit",
            "till_removed",
            "none",
            "before_turn",
            "after_turn",
            "after_round",
            "status",
        ],
    )

    steal_buff_stat_type: Optional[buff_stat_types_enum] = Field(
        default=None,
        title="偷取的buff类型",
        description="偷取的buff类型",
        examples=[
            "hp_heal_received_percent",
            "torchlight_burn_percent",
        ],
    )
    steal_buff_source_type: Optional[buff_sources_enum] = Field(
        default=None,
        title="偷取的buff来源",
        description="偷取的buff来源",
        examples=["bsrc_skill", "bsrc_notspecified", "bsrc_affliction"],
    )
    swap_source_and_target: Optional[bool] = Field(
        default=None,
        title="交换释放源和目标位置",
        description="交换释放源和目标位置",
        examples=[1, 0],
    )
    kill: Optional[int_bool_enum] = Field(
        default=None,
        title="杀死目标",
        description="是否杀死目标",
        examples=[1, 0],
    )
    immobilize: Optional[int_bool_enum] = Field(
        default=None,
        title="无法移动",
        description="是否无法移动",
        examples=[1, 0],
    )
    unimmobilize: Optional[int_bool_enum] = Field(
        default=None,
        title="解除无法移动",
        description="是否解除无法移动",
        examples=[1, 0],
    )
    control: Optional[int] = Field(
        default=None,
        title="控制目标",
        description="控制目标回合数",
        examples=[1, 2, 3],
    )
    uncontrol: Optional[int_bool_enum] = Field(
        default=None,
        title="解除控制",
        description="是否解除控制",
        examples=[1, 0],
    )
    kill_enemy_types: Optional[str] = Field(
        default=None,
        title="杀死指定类型的敌人",
        description="杀死指定类型的敌人",
        examples=["unholy", "man"],
    )
    monsterType: Optional[str] = Field(
        default=None,
        title="生效怪物类型",
        description="对指定怪物类型生效",
        examples=["unholy", "man"],
    )
    capture: Optional[int_bool_enum] = Field(
        default=None,
        title="捕获目标",
        description="是否捕获目标",
        examples=[1, 0],
    )
    capture_remove_from_party: Optional[int_bool_enum] = Field(
        default=None,
        title="从队伍中移除捕获目标",
        description="是否从队伍中移除捕获目标",
        examples=[1, 0],
    )
    disease: Optional[str] = Field(
        default=None, title="疾病", description="施加疾病", examples=["any"]
    )
    remove_vampire: Optional[int_bool_enum] = Field(
        default=None,
        title="移除猩红诅咒",
        description="是否移除猩红诅咒",
        examples=[1, 0],
    )
    summon_monsters: Optional[list[str]] = Field(
        default=None,
        title="召唤怪物",
        description="召唤怪物",
    )
    summon_chances: Optional[list[float]] = Field(
        default=None,
        title="召唤概率",
        description="召唤概率",
    )
    summon_ranks: Optional[list[int]] = Field(
        default=None,
        title="召唤等级",
        description="召唤等级",
    )
    summon_limits: Optional[list[int]] = Field(
        default=None,
        title="召唤限制",
        description="召唤限制",
    )
    summon_count: Optional[int] = Field(
        default=None,
        title="召唤数量",
        description="召唤数量",
    )
    summon_erase_data_on_roll: Optional[int_bool_enum] = Field(
        default=None,
        title="清除召唤数据",
        description="是否清除召唤数据",
        examples=[1, 0],
    )
    summon_can_spawn_loot: Optional[bool] = Field(
        default=None,
        title="允许召唤的怪物生成战利品",
        description="是否允许召唤的怪物生成战利品",
        examples=[1, 0],
    )
    summon_rank_is_previous_monster_class: Optional[bool] = Field(
        default=None,
        title="召唤等级为前一个怪物类型",
        description="是否召唤等级为前一个怪物类型",
        examples=[1, 0],
    )
    summon_does_roll_initiatives: Optional[list[int_bool_enum]] = Field(
        default=None,
        title="召唤的怪物是否自带行动点数",
        description="召唤的怪物是否自带行动点数",
        examples=[[1, 1, 1], [1, 0, 1]],
    )
    crit_doesnt_apply_to_roll: Optional[bool] = Field(
        default=None,
        title="不应用暴击",
        description="是否不应用暴击",
        examples=[1, 0],
    )
    virtue_blockable_chance: Optional[float] = Field(
        default=None,
        title="美德格挡概率？",
        description="美德格挡概率",
        examples=[0.5, 0.5],
    )
    affliction_blockable_chance: Optional[float] = Field(
        default=None,
        title="折磨格挡概率？",
        description="折磨格挡概率",
        examples=[0.5, 0.5],
    )
    set_mode: Optional[str] = Field(
        default=None,
        title="设置模式",
        description="设置模式",
    )
    can_apply_on_death: Optional[bool] = Field(
        default=None,
        title="可以对尸体生效",
        description="是否可以对尸体生效",
        examples=[1, 0],
    )
    apply_once: Optional[bool] = Field(
        default=None,
        title="应用一次?",
        description="是否应用一次",
        examples=[1, 0],
    )
    rank_target: Optional[str] = Field(
        default=None,
        title="标记位置",
        description="标记位置用于延时技能，如先知",
    )
    clear_rank_target: Optional[str] = Field(
        default=None,
        title="清除标记位置",
        description="清除标记位置用于延时技能，如先知",
    )
    performer_rank_target: Optional[int_bool_enum] = Field(
        default=None,
        title="释放源被标记位置",
        description="释放源被标记位置",
        examples=[1, 0],
    )
    apply_with_result: Optional[bool] = Field(
        default=None,
        title="应用结果？",
        description="应用结果",
        examples=[1, 0],
    )
    initiative_change: Optional[int] = Field(
        default=None,
        title="行动点数变化",
        description="行动点数变化",
    )
    source_heal_type: Optional[source_heal_type_enum] = Field(
        default=None,
        title="治疗类型来源",
        description="治疗类型来源",
        examples=[
            "damage_heal",
            "flashback",
            "monster_skill",
            "curio",
            "hero_skill_multi_target",
            "act_out",
            "hero_skill",
            "companion",
            "eat",
            "camp_skill",
            "monster_skill_multi_target",
        ],
    )
    skill_instant: Optional[bool] = Field(
        default=None,
        title="skill_instant",
        description="skill_instant",
        examples=[True, False],
    )
    actor_dot: Optional[str] = Field(
        default=None,
        title="actor_dot",
        description="actor_dot",
    )
    health_damage: Optional[int] = Field(
        default=None,
        title="直接伤害",
        description="直接伤害量",
        examples=[1, 2],
    )
    bark: Optional[str] = Field(
        default=None,
        title="触发语言弹窗",
        description="触发指定语言弹窗",
    )
    set_monster_class_id: Optional[str] = Field(
        default=None,
        title="改变怪物类型",
        description="改变怪物类型为指定类型",
    )
    set_monster_class_ids: Optional[list[str]] = Field(
        default=None,
        title="改变怪物类型",
        description="改变怪物类型为指定类型",
    )
    set_monster_class_chances: Optional[list[float]] = Field(
        default=None,
        title="改变怪物类型几率",
        description="改变怪物类型为指定类型几率",
    )
    set_monster_class_reset_hp: Optional[bool] = Field(
        default=None,
        title="改变怪物类型时重置怪物血量",
        description="改变怪物类型时重置怪物血量",
    )
    set_monster_class_reset_buffs: Optional[bool] = Field(
        default=None,
        title="改变怪物类型时重置怪物buff",
        description="改变怪物类型时重置怪物buff",
    )
    set_monster_class_carry_over_hp_min_percent: Optional[float] = Field(
        default=None,
        title="改变怪物类型时保持怪物血量百分比",
        description="改变怪物类型时保持怪物血量百分比",
    )
    set_monster_class_clear_initative: Optional[bool] = Field(
        default=None,
        title="改变怪物类型时重置怪物行动点数",
        description="改变怪物类型时重置怪物行动点数",
    )
    set_monster_class_clear_monster_brain_cooldowns: Optional[bool] = Field(
        default=None,
        title="改变怪物类型时重置怪物AI冷却",
        description="改变怪物类型时重置怪物AI冷却",
    )
    set_monster_class_reset_scale: Optional[bool] = Field(
        default=None,
        title="改变怪物类型时重置怪物缩放",
        description="改变怪物类型时重置怪物缩放",
    )
    has_description: Optional[bool] = Field(
        default=None,
        title="是否有描述",
        description="是否有描述",
        examples=[True, False],
    )
    stealth: Optional[int_bool_enum] = Field(
        default=None,
        title="潜行",
        description="使目标潜行",
        examples=[1, 0],
    )
    unstealth: Optional[int_bool_enum] = Field(
        default=None,
        title="解除潜行",
        description="使目标解除潜行",
        examples=[1, 0],
    )
    clear_debuff: Optional[int_bool_enum] = Field(
        default=None,
        title="清除debuff",
        description="清除debuff",
        examples=[1, 0],
    )
    health_damage_blocks: Optional[int] = Field(
        default=None,
        title="格挡伤害",
        description="添加格挡伤害次数",
    )
    dotSource: Optional[buff_sources_enum] = Field(
        default=None,
        title="dot源的类型",
        description="dot源的类型",
    )
    buff_source_type: Optional[buff_sources_enum] = Field(
        default=None,
        title="buff源的类型",
        description="buff源的类型",
    )
    use_item_id: Optional[str] = Field(
        default=None,
        title="使用物品",
        description="使用指定id物品",
    )
    use_item_type: Optional[str] = Field(
        default=None,
        title="使用物品",
        description="使用指定类型物品",
    )
    skips_endless_wave_curio: Optional[bool] = Field(
        default=None,
        title="跳过无尽波",
        description="跳过无尽波",
    )
    spawn_target_actor_base_class_id: Optional[str] = Field(
        default=None,
        title="生成目标Actor基类ID？",
    )
    clearvirtue: Optional[int_bool_enum] = Field(
        default=None,
        title="清除美德",
        description="清除美德",
        examples=[1, 0],
    )
    riposte_validate: Optional[bool] = Field(
        default=None,
        title="反击验证",
        description="反击验证",
    )
    buff_is_clear_debuff_valid: Optional[bool] = Field(
        default=None,
        title="buff是否可以清除debuff",
        description="buff是否可以清除debuff",
    )
    refreshes_skill_uses: Optional[bool] = Field(
        default=None,
        title="刷新技能使用次数",
        description="刷新技能使用次数",
    )
    cure_disease: Optional[int_bool_enum] = Field(
        default=None,
        title="治疗疾病",
        description="治疗疾病",
        examples=[1, 0],
    )
    individual_target_actor_rolls: Optional[bool] = Field(
        default=None,
        title="每个目标单独判定",
        description="每个目标单独判定",
    )
    damage_type: Optional[damage_type_enum] = Field(
        default=None,
        title="伤害类型",
        description="伤害类型",
        examples=[
            "attack",
            "bleed",
            "poisoned",
            "obstacle",
            "trap",
            "hunger",
            "captor",
            "healing",
            "ddexit",
            "townexit",
            "additionaleffect",
            "effect",
            "reflect",
            "unknown",
            "",
        ],
    )
    damage_source_type: Optional[damage_source_type_enum] = Field(
        default=None,
        title="伤害源类型",
        description="伤害源类型",
        examples=[
            "monster",
            "friendly",
            "hero",
            "obstacle",
            "trap",
            "hunger",
            "trinket",
            "item",
            "quirk",
            "effect",
            "reflect",
            "unknown",
            "friendly_quirk_actout",
            "friendly_trait_actout",
            "estate_currency",
            "",
        ],
    )
    damage_source_data: Optional[str] = Field(
        default=None,
        title="伤害源数据",
        description="伤害源数据",
    )
    daze: Optional[int_bool_enum] = Field(
        default=None,
        title="眩晕",
        description="眩晕仅限PVP",
    )
    undaze: Optional[int_bool_enum] = Field(
        default=None,
        title="解除眩晕",
        description="解除眩晕仅限PVP",
    )


class data_manager:
    def __init__(self):
        self.effect_id_entries: dict[str, effect] = {}
        self._pk_class: dict[str, type[BaseModel]] = {}
        self._keys_to_type: dict[tuple[str, str], tuple[bool, type]] = {}

        self.init()

    def init(self):
        self._pk_class = {"effect": effect}

        self.init_keys_to_type()

    def init_keys_to_type(self):
        for p_k, cls in self._pk_class.items():
            for s_k, info in cls.model_fields.items():
                is_list = False
                s_ks = [s_k]
                if info.alias:
                    s_ks.append(info.alias)
                if not info.annotation:
                    return None
                annotation = info.annotation
                if get_origin(annotation) is Union:
                    annotation = get_args(annotation)[0]
                    if get_origin(annotation) is list:
                        is_list = True
                        annotation = get_args(annotation)[0]
                if get_origin(annotation) is Literal:
                    annotation = get_args(annotation)[0].__class__
                for s_k in s_ks:
                    self._keys_to_type[(p_k, s_k)] = (is_list, annotation)

    def keys_to_type(self, p_key: str, s_key: str):
        """
        返回一个元组,第一个元素是是否是列表,第二个元素是类型。

        Returns:
                Tuple[bool, type]: 第一个元素是是否是列表，第二个元素是类型。
        """
        return self._keys_to_type.get((p_key, s_key), None)

    def type_check(self, s: str, type: type | UnionType):
        if type is str:
            if (s[0] == '"' and s[-1] == '"') or (s[0] == "'" and s[-1] == "'"):
                return s[1:-1]
            else:
                return s
        if type is float:
            precent_count = s.count("%")
            if precent_count > 0:
                return float(s[:-precent_count]) / 100 * precent_count
            return float(s)
        if type is bool:
            if s.lower() == "true":
                return True
            else:
                return False
        if type is int:
            return int(s)
        if type is int_bool_enum:
            return int(s)
        else:
            raise TypeError(f"未知类型: {type}")

    def get_data_from_str(self, p_key: str, s_key: str, data: list[str]):
        if p_key not in self._pk_class:
            raise ValueError(f"未知表名: {p_key}\n\n\n")
        sk_type = self.keys_to_type(p_key, s_key)
        if not sk_type:
            raise ValueError(f"{p_key} 中未知字段: {s_key}\n\n\n")
        is_list, t = sk_type
        try:
            result = [self.type_check(i, t) for i in data if i != ""]
        except Exception as e:
            raise ValueError(
                f"转换错误 表名: {p_key}, 字段: {s_key}, 值: {data}\n\n{e}\n\n\n"
            ) from e
        if not is_list:
            if len(data) == 0:
                result = 1
            elif len(data) > 1:
                pass
                # raise ValueError(f"数据长度 > 1, 数据长度应该为 1, p_k: {p_key}, s_k: {s_key}, s_v: {data}\n\n")
            else:
                result = result[0]
        return result

    def darkest_paser(self, file_path: str | Path):
        s = Path(file_path).read_text(encoding="utf-8", errors="ignore")
        if not s:
            return
        for darkest_parser_result in darkest.parser_fast(s, self.get_data_from_str):
            if not darkest_parser_result:
                continue
            if isinstance(darkest_parser_result, Exception):
                logger.info(
                    f"{file_path} 解析出现错误：\n{darkest_parser_result}" + "-" * 25
                )
                continue
            p_k, p_entery, pasering_str, start_line, end_line = darkest_parser_result
            try:
                if p_k == "effect":
                    e = effect(**p_entery)  # type: ignore
                    self.effect_id_entries[e.name] = e
                else:
                    logger.info(f"未知表名: {p_k}\n\n\n" + "-" * 25)
                    # raise TypeError(f"unexpected p_k: {p_k}\n\n\n")
            except Exception as e:
                if type(e) is ValidationError:
                    error_info = f"在 {e.title} 中共发现 {e.error_count()} 个错误:\n"
                    for index, i in enumerate(e.errors()):
                        error_info += f"第 {index+1} 个错误\n\t错误字段:\t{i['loc'][0]}\n\t错误类型:\t{i['type']}\n\t错误信息:\t{i['msg']}\n\t输入值:\t\t{i["input"]}\n\t输入值类型:\t{type(i["input"]).__name__}"
                    logger.info(
                        f"{file_path} 解析出现错误：\n{p_k} 解析错误, 位于 {start_line}-{end_line} 行, 错误文本内容: \n\n{pasering_str.strip()}\n\n{error_info}\n\n\n"
                        + "-" * 25
                    )
                    # raise Exception(f"{p_k} 解析错误, 位于 {start_line}-{end_line} 行, 错误文本内容: \n\n{pasering_str.strip()}\n\n{error_info}\n\n\n") from e
