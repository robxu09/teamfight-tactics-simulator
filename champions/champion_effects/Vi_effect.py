# items.item_effects.giant_slayer_effect
from simulation_system.simulation_steps import Simulation_Step

def get_Vi_description():
        description = """Active mana cost 40 / 70
                Deal 330 percentage Attack Damage physical damage to the current target, or 450 percent of AD physical damage 
                if they have more current Health than Vi. Stun them and reduce their Armor for the rest of combat.

                Headliner Effect: +200 Health, +15 percent AD

                Stun Duration: 1.5 / 1.75 / 2
                Armor Reduction: 15% / 18% / 20%"""
        
        return description

# create effect specifically to trigger end of ultimate cast.
# create multiple effects and put in list
# create get_Vi_effects():

def get_Vi_effects():
     
    effects = []

    effects.append(get_Vi_ultimate)
    effects.append(get_Vi_ultimate_end)
    # effects.append(get_Vi_passive_1)
    # effects.append(get_Vi_passive_2)
    
    return effects

# didtrigger: 1 -> start trigger, 0 -> no trigger, -1 -> end trigger
# triggertime: time of start-trigger. on end/no trigger set back to -1
def get_Vi_passive_1():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        if(simulation_step == Simulation_Step.OnDealDamage):
    
            print(f"Vi apologizes for punching {enemy_champion.name}")
            # print(f"{amount_of_times_triggered}, {current_simulation_time}")
            return 1, current_simulation_time
        
        return 0, -1

    return effect

def get_Vi_passive_2():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        if(simulation_step == Simulation_Step.OnDealDamage and int(current_simulation_time)%5 == 0):
    
            print(f"Vi gives {enemy_champion.name} a cookie.")
            # print(f"{amount_of_times_triggered}, {current_simulation_time}")
            return 1, current_simulation_time
        
        return 0, -1

    return effect


def get_Vi_ultimate():
    # data is used to pass in inputs for effects
    def ultimate(simulation_step, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        if(simulation_step == Simulation_Step.OnCastUltimate):
            # gets paused for 1 second after ultimate cast (takes that long to cast)
            # alternate between hugs and kisses


            #                Stun Duration: 1.5 / 1.75 / 2
            #     Armor Reduction: 15% / 18% / 20%
            percentage_reduce_armor = 0
            stun_time = 0

            if(champion.star_level == 3):
                percentage_reduce_armor = 0.2
                stun_time = 2
            elif(champion.star_level == 2):
                percentage_reduce_armor = 0.18
                stun_time = 1.75
            else:
                percentage_reduce_armor = 0.15
                stun_time = 1.5

            # stun and reduce armor
            enemy_champion.set_armor(enemy_champion.armor * (1 - percentage_reduce_armor))

            enemy_champion.set_stun_time(stun_time)

            enemy_champion.become_burned(0.01, stun_time * 2)

            # deal Deal 330 percentage Attack Damage physical damage to the current target, or 450 percent of AD physical damage 
            #    if they have more current Health than Vi. Stun them and reduce their Armor for the rest of combat.
            dmg_to_do = 3.3 * champion.attack_damage
            if (champion.health < enemy_champion.health):

                dmg_to_do = 4.5 * champion.attack_damage

            dmg_to_do = champion.calculate_total_attack_damage_done(dmg_to_do, enemy_champion, champion.can_crit_ult)

            champion.deal_damage(enemy_champion, dmg_to_do)

            # cast time

            champion.is_mana_locked = True
            champion.is_casting_ultimate = True

            # print(f"previous trigger {most_recent_previous_trigger_time}")

            return 1, current_simulation_time
        
        return 0, -1
    
    return ultimate

def get_Vi_ultimate_end():

    # data is used to pass in inputs for effects
    def effect(simulation_step, champion, enemy_champion, current_simulation_time, damage, amount_of_times_triggered=0, most_recent_previous_trigger_time=-1):

        # the order in which the relevant ability is added to effects before being given to champion
        # need to get it's previous cast time
        ultimate_effect_number = 0
        ultimate_activation_time = champion.effects[ultimate_effect_number][2]
        ultimate_cast_duration = 0.1

        if(simulation_step == Simulation_Step.OnStartStatusUpdate):
            
            # print(f"Vi checks if ulting. {champion.effects[ultimate_effect_number][2]}")
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