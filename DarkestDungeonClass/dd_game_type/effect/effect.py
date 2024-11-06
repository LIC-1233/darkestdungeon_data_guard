from pydantic import Field

from DarkestDungeonClass.dd_game_type.base import BaseModel
from DarkestDungeonClass.dd_game_type.enum.type_enum import (
    buff_duration_type_enum,
    buff_sources_enum,
    buff_stat_types_enum,
    damage_source_type_enum,
    damage_type_enum,
    effect_curio_result_type_enum,
    effect_target_enum,
    int_bool_enum,
    keyState_enum,
    source_heal_type_enum,
)


class effect(BaseModel):
    name: str = Field(
        default=None,
        title="effect id",
        description="effect的唯一标识符",
        examples=["Manacles Stun 1"],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    target: effect_target_enum = Field(
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
        json_schema_extra={"format": {"zh-cn": "对{0}"}, "tags": []},
    )
    curio_result_type: effect_curio_result_type_enum = Field(
        default=None,
        title="Curio结果类型",
        description="Curio的结果类型",
        examples=["positive", "negative", "neutral", "none"],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    chance: float = Field(
        default=None,
        title="施加概率",
        description="effect的施加概率",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    on_hit: bool = Field(
        default=None,
        title="命中触发",
        description="effect是否命中触发",
        examples=[True, False],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    on_miss: bool = Field(
        default=None,
        title="未命中触发",
        description="effect是否未命中触发",
        examples=[True, False],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    queue: bool = Field(
        default=None,
        title="effect是否最后结算",
        description="effect是否最后结算",
        examples=[True, False],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dotBleed: int = Field(
        default=None,
        title="流血量",
        description="effect的流血量",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dotPoison: int = Field(
        default=None,
        title="腐蚀量",
        description="effect的腐蚀量",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dotStress: int = Field(
        default=None,
        title="持续加压量",
        description="effect的持续加压量",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stress: int = Field(
        default=None,
        title="加压量",
        description="effect的加压量",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    healstress: int = Field(
        default=None,
        title="减压量",
        description="effect的减压量",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    combat_stat_buff: int_bool_enum = Field(
        default=None,
        title="修改属性",
        description="effect能否修改属性",
        examples=[True, False],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_low_multiply: float = Field(
        default=None,
        title="伤害下限叠乘",
        description="effect的伤害下限叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_low_add: int = Field(
        default=None,
        title="伤害下限叠加",
        description="effect的伤害下限叠加",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_high_multiply: float = Field(
        default=None,
        title="伤害上限叠乘",
        description="effect的伤害上限叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_high_add: int = Field(
        default=None,
        title="伤害上限叠加",
        description="effect的伤害上限叠加",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    max_hp_multiply: float = Field(
        default=None,
        title="最大hp叠乘",
        description="effect的最大hp叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    max_hp_add: int = Field(
        default=None,
        title="最大hp叠加",
        description="effect的最大hp叠加",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    attack_rating_multiply: float = Field(
        default=None,
        title="精准叠乘",
        description="effect的精准叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    attack_rating_add: float = Field(
        default=None,
        title="精准叠加",
        description="effect的精准叠加，注意这里是百分比",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit_chance_multiply: float = Field(
        default=None,
        title="暴击率叠乘",
        description="effect的暴击率叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit_chance_add: float = Field(
        default=None,
        title="暴击率叠加",
        description="effect的暴击率叠加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defense_rating_multiply: float = Field(
        default=None,
        title="闪避叠乘",
        description="effect的闪避叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    defense_rating_add: float = Field(
        default=None,
        title="闪避叠加",
        description="effect的闪避叠加，注意这里是百分比",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    protection_rating_multiply: float = Field(
        default=None,
        title="护甲叠乘",
        description="effect的护甲叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    protection_rating_add: float = Field(
        default=None,
        title="护甲叠加",
        description="effect的护甲叠加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    speed_rating_multiply: float = Field(
        default=None,
        title="速度叠乘",
        description="effect的速度叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    speed_rating_add: float = Field(
        default=None,
        title="速度叠加",
        description="effect的速度叠加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_ids: list[str] = Field(
        default=None,
        title="施加的buff ids",
        description="buff的唯一标识符列表",
        examples=["Manacles Stun 1", "Manacles Stun 2"],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    duration: int = Field(
        default=None,
        title="持续时间",
        description="effect的持续时间",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dotHpHeal: int = Field(
        default=None,
        title="持续治愈量",
        description="effect的持续治愈量",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    heal: int = Field(
        default=None,
        title="治愈量",
        description="effect的治愈量",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    heal_percent: float = Field(
        default=None,
        title="治愈百分比",
        description="effect的治愈百分比",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_crit_heal: bool = Field(
        default=None,
        title="治愈是否可暴击",
        description="effect的治愈是否可以暴击",
        examples=[True, False],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure: int_bool_enum = Field(
        default=None,
        title="治愈腐蚀流血",
        description="effect是否可以治愈目标腐蚀流血",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_bleed: int_bool_enum = Field(
        default=None,
        title="治愈流血",
        description="effect是否可以治愈目标流血",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_poison: int_bool_enum = Field(
        default=None,
        title="治愈腐蚀",
        description="effect是否可以治愈目标腐蚀",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    clearDotStress: int_bool_enum = Field(
        default=None,
        title="清除惊恐",
        description="effect是否可以清除目标惊恐",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    tag: int_bool_enum = Field(
        default=None,
        title="标记",
        description="effect是否可以标记目标",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    untag: int_bool_enum = Field(
        default=None,
        title="清除标记",
        description="effect是否可以清除目标标记",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stun: int_bool_enum = Field(
        default=None,
        title="眩晕",
        description="effect是否可以眩晕目标",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    unstun: int_bool_enum = Field(
        default=None,
        title="清除眩晕",
        description="effect是否可以清除目标眩晕",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    keyStatus: keyState_enum = Field(
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
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte: int_bool_enum = Field(
        default=None,
        title="反击",
        description="是否激活目标反击",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_on_miss_chance_add: float = Field(
        default=None,
        title="反击时闪避概率增加",
        description="反击时闪避概率增加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_on_hit_chance_add: float = Field(
        default=None,
        title="反击时命中概率增加",
        description="反击时命中概率增加",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_on_miss_chance_multiply: float = Field(
        default=None,
        title="反击时闪避概率叠乘",
        description="反击时闪避概率叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_on_hit_chance_multiply: float = Field(
        default=None,
        title="反击时命中概率叠乘",
        description="反击时命中概率叠乘",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_effect: list[str] = Field(
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
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    clear_riposte: int_bool_enum = Field(
        default=None,
        title="清除反击",
        description="effect是否可以清除目标反击",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    guard: int_bool_enum = Field(
        default=None,
        title="守护目标",
        description="是否可以守护目标",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    clearguarding: int_bool_enum = Field(
        default=None,
        title="清除守护",
        description="effect是否可以取消目标守护的状态",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    clearguarded: int_bool_enum = Field(
        default=None,
        title="清除守护",
        description="effect是否可以清除目标被守护的状态",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torch_decrease: int = Field(
        default=None,
        title="减少火把亮度",
        description="减少火把亮度",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    torch_increase: int = Field(
        default=None,
        title="增加火把亮度",
        description="增加火把亮度",
        examples=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    item: int_bool_enum = Field(
        default=None,
        title="来自物品？",
        description="是否来自物品",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    curio: int_bool_enum = Field(
        default=None,
        title="来自饰品？",
        description="是否来自饰品",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dotShuffle: int_bool_enum = Field(
        default=None,
        title="持续乱位",
        description="是否持续乱位",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    push: int = Field(
        default=None,
        title="推后目标",
        description="推后目标",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    pull: int = Field(
        default=None,
        title="拉前目标",
        description="拉前目标",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffletarget: int_bool_enum = Field(
        default=None,
        title="乱位目标",
        description="是否可以乱位目标",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    shuffleparty: int_bool_enum = Field(
        default=None,
        title="乱位整队",
        description="是否可以乱位目标整队",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    instant_shuffle: int_bool_enum = Field(
        default=None,
        title="立即乱位",
        description="是否可以立即乱位",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_amount: float = Field(
        default=None,
        title="buff值",
        description="施加buff的值比如治疗的值",
        examples=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_type: str = Field(
        default=None,
        title="buff类型",
        description="施加buff的类型",
        examples=[
            "hp_heal_received_percent",
            "torchlight_burn_percent",
        ],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_sub_type: str = Field(
        default=None,
        title="buff子类型",
        description="施加buff的子类型",
        examples=[
            "hp_heal_amount",
            "hp_heal_percent",
            "hp_heal_received_percent",
            "riposte_duration_percent	",
        ],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_duration_type: buff_duration_type_enum = Field(
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
    steal_buff_stat_type: buff_stat_types_enum = Field(
        default=None,
        title="偷取的buff类型",
        description="偷取的buff类型",
        examples=[
            "hp_heal_received_percent",
            "torchlight_burn_percent",
        ],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    steal_buff_source_type: buff_sources_enum = Field(
        default=None,
        title="偷取的buff来源",
        description="偷取的buff来源",
        examples=["bsrc_skill", "bsrc_notspecified", "bsrc_affliction"],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    swap_source_and_target: bool = Field(
        default=None,
        title="交换释放源和目标位置",
        description="交换释放源和目标位置",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    kill: int_bool_enum = Field(
        default=None,
        title="杀死目标",
        description="是否杀死目标",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    immobilize: int_bool_enum = Field(
        default=None,
        title="无法移动",
        description="是否无法移动",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    unimmobilize: int_bool_enum = Field(
        default=None,
        title="解除无法移动",
        description="是否解除无法移动",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    control: int = Field(
        default=None,
        title="控制目标",
        description="控制目标回合数",
        examples=[1, 2, 3],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    uncontrol: int_bool_enum = Field(
        default=None,
        title="解除控制",
        description="是否解除控制",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    kill_enemy_types: str = Field(
        default=None,
        title="杀死指定类型的敌人",
        description="杀死指定类型的敌人",
        examples=["unholy", "man"],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    monsterType: str = Field(
        default=None,
        title="生效怪物类型",
        description="对指定怪物类型生效",
        examples=["unholy", "man"],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    capture: int_bool_enum = Field(
        default=None,
        title="捕获目标",
        description="是否捕获目标",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    capture_remove_from_party: int_bool_enum = Field(
        default=None,
        title="从队伍中移除捕获目标",
        description="是否从队伍中移除捕获目标",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    disease: str = Field(
        default=None,
        title="疾病",
        description="施加疾病",
        examples=["any"],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    remove_vampire: int_bool_enum = Field(
        default=None,
        title="移除猩红诅咒",
        description="是否移除猩红诅咒",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_monsters: list[str] = Field(
        default=None,
        title="召唤怪物",
        description="召唤怪物",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_chances: list[float] = Field(
        default=None,
        title="召唤概率",
        description="召唤概率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_ranks: list[int] = Field(
        default=None,
        title="召唤等级",
        description="召唤等级",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_limits: list[int] = Field(
        default=None,
        title="召唤限制",
        description="召唤限制",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_count: int = Field(
        default=None,
        title="召唤数量",
        description="召唤数量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_erase_data_on_roll: int_bool_enum = Field(
        default=None,
        title="清除召唤数据",
        description="是否清除召唤数据",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_can_spawn_loot: bool = Field(
        default=None,
        title="允许召唤的怪物生成战利品",
        description="是否允许召唤的怪物生成战利品",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_rank_is_previous_monster_class: bool = Field(
        default=None,
        title="召唤等级为前一个怪物类型",
        description="是否召唤等级为前一个怪物类型",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    summon_does_roll_initiatives: list[int_bool_enum] = Field(
        default=None,
        title="召唤的怪物是否自带行动点数",
        description="召唤的怪物是否自带行动点数",
        examples=[[1, 1, 1], [1, 0, 1]],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    crit_doesnt_apply_to_roll: bool = Field(
        default=None,
        title="不应用暴击",
        description="是否不应用暴击",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    virtue_blockable_chance: float = Field(
        default=None,
        title="美德格挡概率？",
        description="美德格挡概率",
        examples=[0.5, 0.5],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    affliction_blockable_chance: float = Field(
        default=None,
        title="折磨格挡概率？",
        description="折磨格挡概率",
        examples=[0.5, 0.5],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_mode: str = Field(
        default=None,
        title="设置模式",
        description="设置模式",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    can_apply_on_death: bool = Field(
        default=None,
        title="可以对尸体生效",
        description="是否可以对尸体生效",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    apply_once: bool = Field(
        default=None,
        title="应用一次?",
        description="是否应用一次",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    rank_target: str = Field(
        default=None,
        title="标记位置",
        description="标记位置用于延时技能，如先知",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    clear_rank_target: str = Field(
        default=None,
        title="清除标记位置",
        description="清除标记位置用于延时技能，如先知",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    performer_rank_target: int_bool_enum = Field(
        default=None,
        title="释放源被标记位置",
        description="释放源被标记位置",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    apply_with_result: bool = Field(
        default=None,
        title="应用结果？",
        description="应用结果",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    initiative_change: int = Field(
        default=None,
        title="行动点数变化",
        description="行动点数变化",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    source_heal_type: source_heal_type_enum = Field(
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
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    skill_instant: bool = Field(
        default=None,
        title="skill_instant",
        description="skill_instant",
        examples=[True, False],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    actor_dot: str = Field(
        default=None,
        title="actor_dot",
        description="actor_dot",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    health_damage: int = Field(
        default=None,
        title="直接伤害",
        description="直接伤害量",
        examples=[1, 2],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    bark: str = Field(
        default=None,
        title="触发语言弹窗",
        description="触发指定语言弹窗",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_id: str = Field(
        default=None,
        title="改变怪物类型",
        description="改变怪物类型为指定类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_ids: list[str] = Field(
        default=None,
        title="改变怪物类型",
        description="改变怪物类型为指定类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_chances: list[float] = Field(
        default=None,
        title="改变怪物类型几率",
        description="改变怪物类型为指定类型几率",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_reset_hp: bool = Field(
        default=None,
        title="改变怪物类型时重置怪物血量",
        description="改变怪物类型时重置怪物血量",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_reset_buffs: bool = Field(
        default=None,
        title="改变怪物类型时重置怪物buff",
        description="改变怪物类型时重置怪物buff",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_carry_over_hp_min_percent: float = Field(
        default=None,
        title="改变怪物类型时保持怪物血量百分比",
        description="改变怪物类型时保持怪物血量百分比",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_clear_initative: bool = Field(
        default=None,
        title="改变怪物类型时重置怪物行动点数",
        description="改变怪物类型时重置怪物行动点数",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_clear_monster_brain_cooldowns: bool = Field(
        default=None,
        title="改变怪物类型时重置怪物AI冷却",
        description="改变怪物类型时重置怪物AI冷却",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    set_monster_class_reset_scale: bool = Field(
        default=None,
        title="改变怪物类型时重置怪物缩放",
        description="改变怪物类型时重置怪物缩放",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    has_description: bool = Field(
        default=None,
        title="是否有描述",
        description="是否有描述",
        examples=[True, False],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    stealth: int_bool_enum = Field(
        default=None,
        title="潜行",
        description="使目标潜行",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    unstealth: int_bool_enum = Field(
        default=None,
        title="解除潜行",
        description="使目标解除潜行",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    clear_debuff: int_bool_enum = Field(
        default=None,
        title="清除debuff",
        description="清除debuff",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    health_damage_blocks: int = Field(
        default=None,
        title="格挡伤害",
        description="添加格挡伤害次数",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    dotSource: buff_sources_enum = Field(
        default=None,
        title="dot源的类型",
        description="dot源的类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_source_type: buff_sources_enum = Field(
        default=None,
        title="buff源的类型",
        description="buff源的类型",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    use_item_id: str = Field(
        default=None,
        title="使用物品",
        description="使用指定id物品",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    use_item_type: str = Field(
        default=None,
        title="使用物品",
        description="使用指定类型物品",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    skips_endless_wave_curio: bool = Field(
        default=None,
        title="跳过无尽波",
        description="跳过无尽波",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    spawn_target_actor_base_class_id: str = Field(
        default=None,
        title="生成目标Actor基类ID？",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    clearvirtue: int_bool_enum = Field(
        default=None,
        title="清除美德",
        description="清除美德",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    riposte_validate: bool = Field(
        default=None,
        title="反击验证",
        description="反击验证",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    buff_is_clear_debuff_valid: bool = Field(
        default=None,
        title="buff是否可以清除debuff",
        description="buff是否可以清除debuff",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    refreshes_skill_uses: bool = Field(
        default=None,
        title="刷新技能使用次数",
        description="刷新技能使用次数",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    cure_disease: int_bool_enum = Field(
        default=None,
        title="治疗疾病",
        description="治疗疾病",
        examples=[1, 0],
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    individual_target_actor_rolls: bool = Field(
        default=None,
        title="每个目标单独判定",
        description="每个目标单独判定",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_type: damage_type_enum = Field(
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
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_source_type: damage_source_type_enum = Field(
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
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    damage_source_data: str = Field(
        default=None,
        title="伤害源数据",
        description="伤害源数据",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    daze: int_bool_enum = Field(
        default=None,
        title="眩晕",
        description="眩晕仅限PVP",
        json_schema_extra={"format": {"zh-cn": ""}, "tags": []},
    )
    undaze: int_bool_enum = Field(
        default=None,
        title="解除眩晕",
        description="解除眩晕仅限PVP",
    )


