# items.item_effects.giant_slayer_effect
from simulation_system.simulation_steps import Simulation_Step

def get_giant_slayer_effect_description():
        effect_description = "Deal 25% more damage to enemies with more than 1600 maximum Health."
        return effect_description

def get_giant_slayer_effects():
     
    effects = []

    effects.append(get_giant_slayer_effect)
    
    return effects

def get_giant_slayer_effect():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0):

        effect_trigger_health = 1600
        bonus_damage_percentage = 0.25
    
        if(simulation_step == Simulation_Step.OnDealDamage):

            if(enemy_champion.total_health >= effect_trigger_health):
                print(f"{champion.name} deals 25% more damage more than {damage} because {enemy_champion.name} has {enemy_champion.total_health} total health (more than {effect_trigger_health}).")
                champion.deal_bonus_damage(enemy_champion, damage*bonus_damage_percentage)

                return 1, current_simulation_time
            
        return 0, -1

    return effect