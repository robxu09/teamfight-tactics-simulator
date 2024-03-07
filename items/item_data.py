import copy, csv

# champion_data.py
from items.item import Item

#item effects
from items.item_effects.giant_slayer_effect import get_giant_slayer_effects
from items.item_effects.bloodthirster_effect import get_bloodthirster_effects
from items.item_effects.infinity_edge_effect import get_infinity_edge_effects
from items.item_effects.jeweled_gauntlet_effect import get_jeweled_gauntlet_effects
from items.item_effects.last_whisperer_effect import get_last_whisperer_effects


# Function to create Champion objects with predefined data
def create_items(set, patch):

    # items = {
    #     # component items
    #     "B.F. Sword": Item(name="B.F. Sword", bonus_attack_damage=0.1),
    #     "Chain Vest": Item(name="Chain Vest", bonus_armor=20),
    #     "Giant's Belt": Item(name="Giant's Belt", bonus_health=150),
    #     "Needlessly Large Rod": Item(name="Needlessly Large Rod", bonus_ability_power=10),
    #     "Negatron Cloak": Item(name="Negatron Cloak", bonus_magic_resist=20),
    #     "Recurve Bow": Item(name="Recurve Bow", bonus_attack_speed=0.1),
    #     "Sparring Gloves": Item(name="Sparring Gloves", bonus_critical_strike_chance=0.2),
    #     "Tear of the Goddess": Item(name="Tear of the Goddess", bonus_starting_mana=15),
    #     "Spatula": Item(name="Spatula"),

    #     # completed items
    #     "Deathblade": Item(name="Deathblade", bonus_attack_damage=0.66),
    #     "Bloodthirster": Item(name="Bloodthirster", bonus_attack_damage=0.20, bonus_magic_resist=20, bonus_ability_power=15),
    #     "Giantslayer": Item(name="GiantSlayer", bonus_attack_damage=0.30, bonus_attack_speed=0.10, bonus_ability_power=20),
    #     "Infinity Edge": Item(name="Infinity Edge", bonus_attack_damage=0.35, bonus_critical_strike_chance=0.35),
    #     "Warmog's Armor": Item(name="Warmog's Armor", bonus_health=800),
    #     "Jeweled Gauntlet": Item(name="Jeweled Gauntlet", bonus_ability_power=35, bonus_critical_strike_chance=0.35),
    #     "Last Whisperer": Item(name="Last Whisperer", bonus_attack_speed=0.15, bonus_attack_damage=0.25, bonus_critical_strike_chance=0.2),
    # }

    csv_file_path = 'csv/set_'+ str(set) +'/patch_'+ str(patch) +'/items_base_stats.csv'
    all_items = create_items_from_csv(csv_file_path)
    

    # pass effects to items
    all_items.get("Bloodthirster").set_effects(get_bloodthirster_effects)
    all_items.get("Giant Slayer").set_effects(get_giant_slayer_effects)
    all_items.get("Infinity Edge").set_effects(get_infinity_edge_effects)
    all_items.get("Jeweled Gauntlet").set_effects(get_jeweled_gauntlet_effects)
    all_items.get("Last Whisperer").set_effects(get_last_whisperer_effects)

    return all_items

def create_items_from_csv(file_path):
    items_dict = {}

    with open(file_path, newline='') as csvfile:
        items_data = csv.DictReader(csvfile)


# Name,Description,Is Component,Attack Damage,Ability Power,Armor,Magic Resist,Health,Mana,Attack Speed,Critical Strike Chance
        
        for row in items_data:
            item_name = row['Name']
            items_dict[item_name] = Item(
                name=item_name,
                description=row.get('Description', "No Description"),
                is_component=bool(row.get('Is Component', False)),
                bonus_attack_damage=float(row.get('Attack Damage', 0)),
                bonus_ability_power=float(row.get('Ability Power', 0)),
                bonus_armor=float(row.get('Armor', 0)),
                bonus_magic_resist=float(row.get('Magic Resist', 0)),
                bonus_health=float(row.get('Health', 0)),
                bonus_starting_mana=float(row.get('Mana', 0)),
                bonus_attack_speed=float(row.get('Attack Speed', 0)),
                bonus_critical_strike_chance=float(row.get('Critical Strike Chance', 0))
            )

    return items_dict