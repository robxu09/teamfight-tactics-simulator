# champion_data.py
import sys

from champions.champion import Champion

from champions.champion_effects.Vi_effect import get_Vi_effects, get_Vi_description

# Function to create Champion objects with predefined data
def create_champions():
    champions = {
        "Annie": Champion(name="Annie", health=450, starting_mana=0, mana_to_cast=50, attack_damage=40, ability_power=100, armor=20, 
                        magic_resist=20, attack_speed=0.65),
        "Tahm Kench": Champion(name="Tahm Kench", health=650, starting_mana=0, mana_to_cast=sys.maxsize, attack_damage=88, ability_power=100, 
                        armor=40, magic_resist=40, attack_speed=0.55),
        "Vi": Champion(name="Vi", health=650, starting_mana=40, mana_to_cast=70, attack_damage=45, ability_power=45, armor=45, magic_resist=45, 
                        attack_speed=0.6, description=get_Vi_description),
    }

    # pass effect to champions
    champions.get("Vi").set_effects(get_Vi_effects)
    
    return champions