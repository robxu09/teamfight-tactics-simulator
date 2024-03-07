import copy

# champion_data.py
from items.item import Item

#item effects
from items.item_effects.giant_slayer_effect import get_giant_slayer_effects, get_giant_slayer_effect_description
from items.item_effects.bloodthirster_effect import get_bloodthirster_effects, get_bloodthirster_effect_description
from items.item_effects.infinity_edge_effect import get_infinity_edge_effects, get_infinity_edge_effect_description
from items.item_effects.jeweled_gauntlet_effect import get_jeweled_gauntlet_effects, get_jeweled_gauntlet_effect_description
from items.item_effects.last_whisperer_effect import get_last_whisperer_effects, get_last_whisperer_description


# Function to create Champion objects with predefined data
def create_items():

    items = {
        # component items
        "B.F. Sword": Item(name="B.F. Sword", bonus_attack_damage=0.1),
        "Chain Vest": Item(name="Chain Vest", bonus_armor=20),
        "Giant's Belt": Item(name="Giant's Belt", bonus_health=150),
        "Needlessly Large Rod": Item(name="Needlessly Large Rod", bonus_ability_power=10),
        "Negatron Cloak": Item(name="Negatron Cloak", bonus_magic_resist=20),
        "Recurve Bow": Item(name="Recurve Bow", bonus_attack_speed=0.1),
        "Sparring Gloves": Item(name="Sparring Gloves", bonus_critical_strike_chance=0.2),
        "Tear of the Goddess": Item(name="Tear of the Goddess", bonus_starting_mana=15),
        "Spatula": Item(name="Spatula"),

        # completed items
        "Deathblade": Item(name="Deathblade", bonus_attack_damage=0.66),
        "Bloodthirster": Item(name="Bloodthirster", bonus_attack_damage=0.20, bonus_magic_resist=20, bonus_ability_power=15, 
                    bonus_omnivamp=0.2, effect_description=get_bloodthirster_effect_description),
        "Giantslayer": Item(name="GiantSlayer", bonus_attack_damage=0.30, bonus_attack_speed=0.10, bonus_ability_power=20, 
                            effect_description=get_giant_slayer_effect_description),
        "Infinity Edge": Item(name="Infinity Edge", bonus_attack_damage=0.35, bonus_critical_strike_chance=0.35, 
                            effect_description=get_infinity_edge_effect_description),
        "Warmog's Armor": Item(name="Warmog's Armor", bonus_health=800),
        "Jeweled Gauntlet": Item(name="Jeweled Gauntlet", bonus_ability_power=35, bonus_critical_strike_chance=0.35, 
                            effect_description=get_jeweled_gauntlet_effect_description),
        "Last Whisperer": Item(name="Last Whisperer", bonus_attack_speed=0.15, bonus_attack_damage=0.25, bonus_critical_strike_chance=0.2,
                            effect_description=get_last_whisperer_description),
    }

    # pass effects to items
    items.get("Bloodthirster").set_effects(get_bloodthirster_effects)
    items.get("Giantslayer").set_effects(get_giant_slayer_effects)
    items.get("Infinity Edge").set_effects(get_infinity_edge_effects)
    items.get("Jeweled Gauntlet").set_effects(get_jeweled_gauntlet_effects)
    items.get("Last Whisperer").set_effects(get_last_whisperer_effects)

    return items