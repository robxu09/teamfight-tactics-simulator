# champion_data.py
import sys

from champions.champion import Champion

from champions.champion_effects.Vi_effect import get_Vi_effects, get_Vi_description

# Function to create Champion objects with predefined data
def create_champions():
    champions = {
        "Tahm Kench": Champion(name="Tahm Kench", health=650, attack_damage=70, armor=40, attack_speed=0.55, starting_mana=0, 
                               mana_to_cast=sys.maxsize, mana_gained_on_hit=0, mana_gained_on_attack=0),
        "Vi": Champion(name="Vi", health=650, attack_damage=55, armor=45, attack_speed=0.6, starting_mana=40, mana_to_cast=70, 
                       mana_gained_on_attack=10, mana_gained_on_hit=1, description=get_Vi_description),
    }

    # pass effect to champions
    champions.get("Vi").set_effects(get_Vi_effects)
    
    return champions