# items.item_effects.last_whisperer_effect
from simulation_system.simulation_steps import Simulation_Step

def get_last_whisperer_effects():
     
    effects = []

    effects.append(get_last_whisperer_effect_activation)
    effects.append(get_last_whisperer_effect_end)
    
    return effects

def get_last_whisperer_effect_activation():

    # data is used to pass in inputs for effects
    # returns didtrigger, triggertime
    # didtrigger: 1 -> start trigger, 0 -> no trigger, -1 -> end trigger
    # triggertime: time of start-trigger. on end/no trigger set back to -1

    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):
        # print(f"hello BT shield! {current_simulation_time}")
        sunder_percentage = 0.3

        # handle effect trigger start
        if(simulation_step == Simulation_Step.BeforeDealDamage):
            
            # print(f"sunder! {current_simulation_time}")
            enemy_champion.set_sunder_amount(sunder_percentage)

            return 1, current_simulation_time  
        
        return 0, -1

    return effect

def get_last_whisperer_effect_end():
    
    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):
        # print(f"{current_simulation_time}")

        effect_duration_time = 3

        activation_time = item.effects[0][2]

        # handle effect end
        if(simulation_step == Simulation_Step.OnEndStatusUpdate):

            if(activation_time > 0 and current_simulation_time >= activation_time + effect_duration_time and activation_time > most_recent_previous_trigger_time):

                enemy_champion.set_sunder_amount(0)
                # print(f"end {most_recent_previous_trigger_time}")
                return 1, current_simulation_time 
            
        return 0, -1
            
    return effect