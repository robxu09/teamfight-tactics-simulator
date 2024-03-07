# champion_data.py
import sys, csv

from champions.champion import Champion

from champions.champion_effects.Annie_effect import get_Annie_effects, get_Annie_description
from champions.champion_effects.Vi_effect import get_Vi_effects, get_Vi_description

# Function to create Champion objects with predefined data
def create_champions(set, patch):
    champions = {
        "Annie": Champion(name="Annie", health=450, starting_mana=0, mana_to_cast=50, attack_damage=40, ability_power=100, armor=20, 
                        magic_resist=20, attack_speed=0.65, description=get_Annie_description),
        "Tahm Kench": Champion(name="Tahm Kench", health=650, starting_mana=0, mana_to_cast=sys.maxsize, attack_damage=88, ability_power=100, 
                        armor=40, magic_resist=40, attack_speed=0.55),
        "Vi": Champion(name="Vi", health=650, starting_mana=40, mana_to_cast=70, attack_damage=45, ability_power=45, armor=45, magic_resist=45, 
                        attack_speed=0.6, description=get_Vi_description),
    }

    
    # # Example usage:
    # csv_file_path = 'csv/set_'+ str(set) +'/patch_'+ str(patch) +'/champions_base_stats.csv'
    # all_champions = create_champions_from_csv(csv_file_path)

    # # pass effect to champions
    # all_champions.get("Annie_1").set_effects(get_Annie_effects)
    # all_champions.get("Vi_1").set_effects(get_Vi_effects)
    
    return champions

def create_champions_from_csv(file_path):
    champions_dict = {}

    with open(file_path, newline='') as csvfile:
        champions_data = csv.DictReader(csvfile)
        # Name	Star Level	Health	Attack Damage	Ability Power	Armor	Magic Resist	Attack Speed	Starting Mana	Mana to Cast	Attack Range
        for row in champions_data:
            champion_name = row['Name']
            champion_star_level=row['Star Level']
            champions_dict[champion_name+'_'+champion_star_level] = Champion(
                name=champion_name,
                star_level=int(row.get('Star Level')),
                health=float(row.get('Health', 0)),
                attack_damage=float(row.get('Attack Damage', 0)),
                ability_power=float(row.get('Ability Power', 0)),
                armor=float(row.get('Armor', 0)),
                magic_resist=float(row.get('Magic Resist', 0)),
                attack_speed=float(row.get('Attack Speed', 0)),
                attack_range=int(row.get('Starting Mana', 0)),
                starting_mana=int(row.get('Starting Mana', 0)),
                mana_to_cast=int(row.get('Starting Mana', 0)),
            )

    return champions_dict
