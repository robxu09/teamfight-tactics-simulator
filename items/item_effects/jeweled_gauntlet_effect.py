# items.item_effects.jeweled_gauntlet_effectpass
from simulation_system.simulation_steps import Simulation_Step

def get_jeweled_gauntlet_effect_description():
        effect_description = "Abilities can critically strike.\n\nIf the holder's abilities can already critically strike, gain 10% Critical Strike Damage instead."
        return effect_description

def get_jeweled_gauntlet_effects():
     
    effects = []

    effects.append(get_jeweled_gauntlet_effect)
    
    return effects

def get_jeweled_gauntlet_effect():

    # data is used to pass in inputs for effects
    def effect(simulation_steps, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0):

        pass

    return effect