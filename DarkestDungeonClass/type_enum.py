from typing import Literal

target_enum = Literal[
    "performer",
    "performer_group",
    "performer_group_other",
    "target",
    "target_group",
    "target_group_other",
    "target_enemy_group",
    "global",
]
curio_result_type_enum = Literal["positive", "negative", "neutral", "none"]
keyState_enum = Literal[
    "tagged",
    "poisoned",
    "bleeding",
    "stunned",
    "dazed",
    "virtued",
    "afflicted",
    "transformed",
]
buff_stat_types_enum = Literal[
    "hp_heal_amount",
    "hp_heal_percent",
    "hp_heal_received_percent",
    "combat_stat_multiply",
    "combat_stat_add",
    "resistance",
    "poison_chance",
    "bleed_chance",
    "stress_dmg_percent",
    "stress_dmg_received_percent",
    "stress_heal_percent",
    "stress_heal_received_percent",
    "party_surprise_chance",
    "monsters_surprise_chance",
    "ambush_chance",
    "scouting_chance",
    "starving_damage_percent",
    "upgrade_discount",
    "damage_received_percent",
    "debuff_chance",
    "resolve_check_percent",
    "stun_chance",
    "move_chance",
    "remove_negative_quirk_chance",
    "food_consumption_percent",
    "resolve_xp_bonus_percent",
    "activity_side_effect_chance",
    "vampire_evolution_duration",
    "quirk_evolution_death_immune",
    "disable_combat_skill_attribute",
    "guard_blocked",
    "tag_blocked",
    "ignore_protection",
    "ignore_stealth",
    "crit_received_chance",
    "riposte",
    "tag",
    "stealth",
    "hp_dot_bleed",
    "hp_dot_poison",
    "hp_dot_heal",
    "stress_dot",
    "shuffle_dot",
    "guarded",
    "status",
    "vampire",
    "torch_increase_percent",
    "torch_decrease_percent",
    "torchlight_burn_percent",
    "stress_on_miss",
    "stress_from_idle_in_town",
    "shard_reward_percent",
    "shard_consume_percent",
    "damage_reflect_percent",
    "hp_dot_bleed_duration_received_percent",
    "hp_dot_bleed_duration_percent",
    "hp_dot_bleed_amount_received_percent",
    "hp_dot_bleed_amount_percent",
    "hp_dot_poison_duration_received_percent",
    "hp_dot_poison_duration_percent",
    "hp_dot_poison_amount_received_percent",
    "hp_dot_poison_amount_percent",
    "stress_dot_duration_received_percent",
    "stress_dot_duration_percent",
    "stress_dot_amount_received_percent",
    "stress_dot_amount_percent",
    "hp_heal_dot_duration_received_percent",
    "hp_heal_dot_duration_percent",
    "hp_heal_dot_amount_received_percent",
    "hp_heal_dot_amount_percent",
    "shuffle_dot_duration_received_percent",
    "shuffle_dot_duration_percent",
    "guard_duration_received_percent",
    "guard_duration_percent",
    "cure_bleed_received_chance",
    "cure_poison_received_chance",
    "cure_bleed_chance",
    "cure_poison_chance",
    "random_target_friendly_chance",
    "random_target_attack_chance",
    "transfer_debuff_from_attacker_chance",
    "transfer_buff_from_attacker_chance",
    "quirk_tag_evolution_duration",
    "deathblow_chance",
    "heartattack_stress_heal_percent",
    "ignore_guard",
    "buff_duration_percent",
    "riposte_duration_percent",
]
buff_sources_enum = Literal["bsrc_skill","bsrc_notspecified","bsrc_affliction","bsrc_virtue","bsrc_item","bsrc_curio","bsrc_disease","bsrc_riposte","bsrc_campingskill","bsrc_quirk","bsrc_trinket","bsrc_trinket_set","bsrc_instantSkill","bsrc_guard","bsrc_deathsdoor","bsrc_deathsdoor_recovery","bsrc_deathsdoor_recovery_heart_attack","bsrc_quest_failure","bsrc_companion","bsrc_stun","bsrc_town","bsrc_district","bsrc_torchsettings","bsrc_crit","bsrc_trinket_additional_effect","bsrc_battle_modifier","bsrc_never_again","bsrc_vampire","bsrc_town_event","bsrc_flashback_start","bsrc_flashback_result","bsrc_completed_darkest_dungeon_quest_party_hero","bsrc_last_hero","bsrc_quest_modifier","combat_end"]
source_heal_type_enum = Literal[
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
]
damage_type_enum = Literal[
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
]
damage_source_type_enum = Literal[
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
]
buff_duration_type_enum = Literal[
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
]
int_bool_enum = Literal[1, 0]