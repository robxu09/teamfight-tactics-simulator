import copy, csv

# champion_data.py
from items.item import Item

#item effects
from items.set_10.item_effects.giant_slayer_effect import get_giant_slayer_effects
from items.set_10.item_effects.bloodthirster_effect import get_bloodthirster_effects
from items.set_10.item_effects.infinity_edge_effect import get_infinity_edge_effects
from items.set_10.item_effects.jeweled_gauntlet_effect import get_jeweled_gauntlet_effects
from items.set_10.item_effects.last_whisper_effect import get_last_whisper_effects


# Function to create Champion objects with predefined data
def create_items(set, patch):

    csv_file_path = 'csv/set_'+ str(set) +'/patch_'+ str(patch) +'/items.csv'
    all_items = create_items_from_csv(csv_file_path)
    

    # pass effects to items
    all_items.get("Bloodthirster").set_effects(get_bloodthirster_effects)
    all_items.get("Giant Slayer").set_effects(get_giant_slayer_effects)
    all_items.get("Infinity Edge").set_effects(get_infinity_edge_effects)
    all_items.get("Jeweled Gauntlet").set_effects(get_jeweled_gauntlet_effects)
    all_items.get("Last Whisper").set_effects(get_last_whisper_effects)

    return all_items

def create_items_from_csv(file_path):
    items_dict = {}

    with open(file_path, newline='') as csvfile:
        items_data = csv.DictReader(csvfile)


# name,attack damage,ability power,armor,magic resist,health,mana,attack speed,critical strike chance,description
        
        for row in items_data:
            item_name = row['name']
            items_dict[item_name] = Item(
                name=item_name,
                description=row.get('description', "No Description"),
                bonus_attack_damage=float(row.get('attack damage', 0)),
                bonus_ability_power=float(row.get('ability power', 0)),
                bonus_armor=float(row.get('armor', 0)),
                bonus_magic_resist=float(row.get('magic resist', 0)),
                bonus_health=float(row.get('health', 0)),
                bonus_starting_mana=float(row.get('mana', 0)),
                bonus_attack_speed=float(row.get('attack speed', 0)),
                bonus_critical_strike_chance=float(row.get('critical strike chance', 0))
            )

    return items_dict