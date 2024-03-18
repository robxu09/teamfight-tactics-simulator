# items.item_effects.giant_slayer_effect
from simulation_system.simulation_steps import Simulation_Step

def get_giant_slayer_effects():
     
    effects = []

    effects.append(get_giant_slayer_effect)
    
    return effects

def get_giant_slayer_effect():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):
    
        if(simulation_step == Simulation_Step.OnDealDamage):

            effect_trigger_health = 1600
            bonus_damage_percentage = 0.25

            if(enemy_champion.total_health >= effect_trigger_health):

                # print(f"{champion.name} deals 25% more damage more than {damage} because {enemy_champion.name} has {enemy_champion.total_health} total health (more than {effect_trigger_health}).")
                champion.deal_bonus_damage(enemy_champion, damage[0]*bonus_damage_percentage, damage[1])

                return 1, current_simulation_time
            
        return 0, -1

    return effect