# items.item_effects.infinity_edge_effect
from simulation_system.simulation_steps import Simulation_Step

def get_infinity_edge_effect_description():
        effect_description = "Abilities can critically strike.\n\nIf the holder's abilities can already critically strike, gain 10% Critical Strike Damage instead."
        return effect_description

def get_infinity_edge_effects():
     
    effects = []

    effects.append(get_infinity_edge_effect)
    
    return effects

def get_infinity_edge_effect():

    # data is used to pass in inputs for effects
    def effect(simulation_steps, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0):

        pass

    return effect