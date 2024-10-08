# items.item_effects.bloodthirster_effect
from simulation_system.simulation_steps import Simulation_Step

def get_bloodthirster_effects():
     
    effects = []

    effects.append(get_bloodthirster_effect_activation)
    effects.append(get_bloodthirster_effect_passive)
    
    return effects

def get_bloodthirster_effect_activation():

    # data is used to pass in inputs for effects
    # returns didtrigger, triggertime
    # didtrigger: 1 -> start trigger, 0 -> no trigger, -1 -> end trigger
    # triggertime: time of start-trigger. on end/no trigger set back to -1

    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        if(simulation_step == Simulation_Step.OnStartStatusUpdate):

            effect_trigger_percentage_health = 0.4
            max_health_shield_percentage = 0.25
            number_of_times_effect_can_trigger = 1
            shield_up_time = 5

            if(amount_of_times_triggered < number_of_times_effect_can_trigger and champion.health <= champion.max_health * effect_trigger_percentage_health):

                champion.deal_shielding(champion, max_health_shield_percentage * champion.max_health, shield_up_time)
                # print(f'bt active: {max_health_shield_percentage * champion.max_health}')

                return 1, current_simulation_time  
        
        return 0, most_recent_previous_trigger_time

    return effect

def get_bloodthirster_effect_passive():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        if(simulation_step == Simulation_Step.OnInitiation):
            
            omnivamp_bonus = 0.2
            champion.omnivamp += omnivamp_bonus
            return 1, current_simulation_time

        return 0, -1             

    return effect