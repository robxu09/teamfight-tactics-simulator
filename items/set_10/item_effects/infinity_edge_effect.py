# items.item_effects.infinity_edge_effect
from simulation_system.simulation_steps import Simulation_Step

def get_infinity_edge_effects():
     
    effects = []

    effects.append(get_infinity_edge_effect)
    
    return effects

def get_infinity_edge_effect():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        if(simulation_step == Simulation_Step.OnInitiation):

            champion.can_crit_ult = True
            if(champion.can_crit_ult_default == True):
                champion.critical_strike_damage += 0.1
            return 1, current_simulation_time

        return 0, -1  

    return effect