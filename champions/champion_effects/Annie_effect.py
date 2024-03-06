# champions.champion_effects.Annie_effect
from simulation_system.simulation_steps import Simulation_Step

def get_Annie_description():
        description = """Passive: After 4 casts, gain 40% Attack Speed and casts deal 80/120/180 () magic damage to another nearby enemy.

Active: Deal 220/330/495 () magic damage to the current target."""
        
        return description

# create effect specifically to trigger end of ultimate cast.
# create multiple effects and put in list
# create get_Annie_effects():

def get_Annie_effects():
     
    effects = []

    effects.append(get_Annie_ultimate)
    effects.append(get_Annie_ultimate_end)
    
    return effects

# didtrigger: 1 -> start trigger, 0 -> no trigger, -1 -> end trigger
# triggertime: time of start-trigger. on end/no trigger set back to -1


def get_Annie_ultimate():
    # data is used to pass in inputs for effects
    def ultimate(simulation_step, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        if(simulation_step == Simulation_Step.OnCastUltimate):

            # 220/330/495

            dmg_to_do = 0
            bonus_dmg_to_do = 0

            amount_of_times_before_bonus = 4

            if(champion.star_level == 3):
                dmg_to_do = 495
                bonus_dmg_to_do = 180
            elif(champion.star_level == 2):
                dmg_to_do = 330
                bonus_dmg_to_do = 120
            else:
                dmg_to_do = 220
                bonus_dmg_to_do = 80



            dmg_to_do = champion.calculate_total_magic_damage_done(dmg_to_do, enemy_champion, champion.can_crit_ult)

            champion.deal_damage(enemy_champion, dmg_to_do)
            # print(f"{champion.name} casted {amount_of_times_triggered} times before this")

            if (amount_of_times_triggered >= amount_of_times_before_bonus):
                # print("bonus cast")

                # implement bonus damage
                bonus_dmg_to_do = champion.calculate_total_magic_damage_done(bonus_dmg_to_do, enemy_champion, champion.can_crit_ult)

                champion.deal_damage(enemy_champion, bonus_dmg_to_do)

                pass

            # cast time

            champion.is_mana_locked = True
            champion.is_casting_ultimate = True

            # print(f"previous trigger {most_recent_previous_trigger_time}")

            return 1, current_simulation_time
        
        return 0, -1
    
    return ultimate

def get_Annie_ultimate_end():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        # the order in which the relevant ability is added to effects before being given to champion
        # need to get it's previous cast time
        ultimate_effect_number = 0
        ultimate_activation_time = champion.effects[ultimate_effect_number][2]
        ultimate_cast_duration = 0.1

        if(simulation_step == Simulation_Step.OnStartStatusUpdate):
            
            # print(f"Annie checks if ulting. {champion.effects[ultimate_effect_number][2]}")
            if(current_simulation_time <= ultimate_activation_time + ultimate_cast_duration):
                champion.is_mana_locked = True
                champion.is_casting_ultimate = True
                # print(f"{champion.name} is casting ultimate. {round(champion.effects[ultimate_effect_number][2] + ultimate_cast_duration - current_simulation_time,2)} seconds left")

            else:
                champion.is_mana_locked = False
                champion.is_casting_ultimate = False

                return 1, current_simulation_time

        
        return 0, -1

    return effect