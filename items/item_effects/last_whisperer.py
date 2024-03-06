# items.item_effects.last_whisperer_effect
from simulation_system.simulation_steps import Simulation_Step

def get_last_whisperer_description():
        effect_description = """Gain 20% Omnivamp.
                Once per combat at 40% Health, gain a 25% max Health Shield that lasts up to 5 seconds."""""
                
        return effect_description

def get_last_whisperer_effects():
     
    effects = []

    effects.append(get_last_whisperer_effect)
    effects.append(get_last_whisperer_effect_end)
    
    return effects

def get_last_whisperer_effect():

    # data is used to pass in inputs for effects
    # returns didtrigger, triggertime
    # didtrigger: 1 -> start trigger, 0 -> no trigger, -1 -> end trigger
    # triggertime: time of start-trigger. on end/no trigger set back to -1

    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):
        # print(f"hello BT shield! {current_simulation_time}")
        effect_trigger_percentage_health = 0.4
        max_health_shield_percentage = 0.25
        number_of_times_effect_can_trigger = 1

        # handle effect trigger start
        if(simulation_step == Simulation_Step.OnStatusUpdate):
            (f"Amount of times! {amount_of_times_triggered}")
            if(amount_of_times_triggered < number_of_times_effect_can_trigger and champion.health <= champion.total_health * effect_trigger_percentage_health):
                print(f"Start BT shield! {current_simulation_time}")
                champion.shield += max_health_shield_percentage * champion.total_health
                return 1, current_simulation_time  
        
        return 0, -1

    return effect

def get_last_whisperer_effect_end():
    
    def effect(simulation_step, champion, enemy_champion, item, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):
        # print(f"{current_simulation_time}")
        effect_duration_time = 5
        max_health_shield_percentage = 0.25

        # handle effect end
        if(simulation_step == Simulation_Step.OnStatusUpdate):
            if(amount_of_times_triggered < 1 and item.effects[0][2] > 0 and current_simulation_time >= item.effects[0][2] + effect_duration_time):
                champion.shield -= max_health_shield_percentage * champion.total_health
                if(champion.shield < 0):
                    champion.shield = 0
                print(f"End BT shield! {current_simulation_time}")
                return 1, current_simulation_time 
        return 0, -1
            
    return effect