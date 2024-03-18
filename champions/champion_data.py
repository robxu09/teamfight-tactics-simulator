# champion_data.py
import sys, csv, re

from champions.champion import Champion

from champions.set_10.champion_effects.Annie_effect import get_Annie_effects
from champions.set_10.champion_effects.Vi_effect import get_Vi_effects

# Function to create Champion objects with predefined data
def create_champions(set, patch):

    csv_file_path = 'csv/set_'+ str(set) +'/patch_'+ str(patch) +'/champions.csv'
    all_champions = create_champions_from_csv(csv_file_path)

    # # # # pass effect to champions
    all_champions.get("Annie_1").set_effects(get_Annie_effects)
    all_champions.get("Annie_2").set_effects(get_Annie_effects)
    all_champions.get("Vi_1").set_effects(get_Vi_effects)
    
    return all_champions

def create_champions_from_csv(file_path):
    champions_dict = {}

    with open(file_path, newline='') as csvfile:
        champions_data = csv.DictReader(csvfile)
        # name,cost,traits,health,attack damage,ability power,attack speed,armor,magic resist,attack range,starting mana,mana to cast,description
        for row in champions_data:
                
            for star in [1,2,3]:
                champion_name = row['name'] + "_" + str(star)
                champions_dict[champion_name] = Champion(
                    name=champion_name,
                    star_level=star,
                    cost=int(row.get('cost')),
                    traits=list(row.get('traits')),
                    health=extract_number(row.get('health', 0), star),
                    attack_damage=extract_number(row.get('attack damage', 0), star),
                    ability_power=float(row.get('ability power', 0)),
                    armor=float(row.get('armor', 0)),
                    magic_resist=float(row.get('magic resist', 0)),
                    attack_speed=float(row.get('attack speed', 0)),
                    attack_range=row.get('attack range', 0),
                    starting_mana=int(row.get('starting mana', 0)),
                    mana_to_cast=int(row.get('mana to cast', 0)),
                    description=row.get('description', '')
                )

    return champions_dict

def extract_number(input_str, index):
    # Define the regular expression pattern
    pattern = r'\b\d+\b'

    # Find all numbers in the string
    numbers = re.findall(pattern, input_str)

    # Check if the index is within range
    if 1 <= index <= len(numbers):
        return int(numbers[index - 1])  # Return the number at the specified index
    else:
        return None  # Return None if index is out of range
