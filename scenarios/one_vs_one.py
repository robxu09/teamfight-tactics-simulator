# entities/one_vs_one.py

import numpy as np

from simulation_system.simulation_steps import Simulation_Step
from simulation_system.simulation_timer import SimulationTimer
from simulation_system.simulation_results import SimulationResults

class OneVsOne:
    def __init__(self):
        self.description = "A one versus one scenario with two champions fighting."

    def run(self, champion1, champion2, time_in_seconds=5):

        # create timer
        timer = self.start_up_set_up(champion1, champion2, time_in_seconds)
        # one tick is .05 seconds
        while(timer.current_time < timer.end_time):

            # Champions update their status at start
            champion1.update_status_start(champion2)
            champion2.update_status_start(champion1)

            # Simulate ultimate casts if ready
            champion1.cast_ultimate_if_possible(champion2)
            champion2.cast_ultimate_if_possible(champion1)

            # Simulate autoattacks if ready
            champion1.autoattack_if_possible(champion2)

            champion2.autoattack_if_possible(champion1)

            # end the fight if one dies
            if champion2.health <= 0:
                print(f"{champion2.name} has been defeated!")
                break

            if champion1.health <= 0:
                print(f"{champion1.name} has been defeated!")
                break
            
            # champions update their status at end
            champion1.update_status_end(champion2)
            champion2.update_status_end(champion1)
            
            # print(f"Timer: {round(timer.current_time,2)}")
            # increment simulation timer
            timer.increment_timer()

            # end of loop

        # self.print_stats(champion1, champion2)
        self.sim_results = SimulationResults([champion1, champion2], timer)
        self.sim_results.populate_results()
        self.sim_results.print_results()

    # start up helper method
        # creates timer, attaches timer to champions, and activates initial effects
        # returns timer
    def start_up_set_up(self, champion1, champion2, time_in_seconds=5):
        # create timer
        timer = SimulationTimer(0, time_in_seconds)

        print(f"Scenario: {self.description}")
        print(f"{champion1.name} vs. {champion2.name}")

        # attach timer to champions
        champion1.timer = timer
        champion2.timer = timer

        # run initial effects
        champion1.activate_effects(Simulation_Step.OnInitiation, champion2, 0)
        champion2.activate_effects(Simulation_Step.OnInitiation, champion1, 0)

        return timer
    
    def print_stats(self, champion1, champion2):
        print("\nFight Stats:")
        print("\nRemaining Health:")
        print(f"{champion1.name} has {round(champion1.stat_tracker.champion.health,3)} health remaining.")
        print(f"{champion2.name} has {round(champion2.stat_tracker.champion.health,3)} health remaining.")


        print("\nTotal Damage Dealt:")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.total_damage_done,3)} damage.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.ad_damage_done,3)} AD damage.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.ap_damage_done,3)} AP damage.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.true_damage_done,3)} True damage.")

        print(f"{champion2.name} dealt {round(champion2.stat_tracker.total_damage_done,3)} damage.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.ad_damage_done,3)} AD damage.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.ap_damage_done,3)} AP damage.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.true_damage_done,3)} True damage.")
        
        print(f"\nDamage Dealt to Direct Opponent:")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.total_damage_done_to_target,3)} damage to {champion2.name}.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.ad_damage_done_to_target,3)} AD damage to {champion2.name}.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.ap_damage_done_to_target,3)} AP damage to {champion2.name}.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.true_damage_done_to_target,3)} True damage to {champion2.name}.")

        print(f"{champion2.name} dealt {round(champion2.stat_tracker.total_damage_done_to_target,3)} damage to {champion1.name}.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.ad_damage_done_to_target,3)} AD damage to {champion1.name}.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.ap_damage_done_to_target,3)} AP damage to {champion1.name}.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.true_damage_done_to_target,3)} True damage to {champion1.name}.")

        print(f"\nDamage Dealt to Others:")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.total_damage_done_to_target,3)} damage to others.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.ad_damage_done_to_target,3)} AD damage to others.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.ap_damage_done_to_target,3)} AP damage to others.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.true_damage_done_to_target,3)} True damage to others.")

        print(f"{champion2.name} dealt {round(champion2.stat_tracker.total_damage_done_to_target,3)} damage to others.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.ad_damage_done_to_target,3)} AD damage to others.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.ap_damage_done_to_target,3)} AP damage to others.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.true_damage_done_to_target,3)} True damage to others.")

        print("\nDamage Taken:")
        print(f"{champion1.name} took {round(champion1.stat_tracker.total_damage_taken,3)} damage.")
        print(f"{champion2.name} took {round(champion2.stat_tracker.total_damage_taken,3)} damage.")

        print("\nHealing Done:")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.total_healed,3)} healing.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.amount_healed_to_self,3)} healing to self.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.amount_healed_to_others,3)} healing to others.")

        print(f"{champion2.name} dealt {round(champion2.stat_tracker.total_healed,3)} healing.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.amount_healed_to_self,3)} healing to self.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.amount_healed_to_others,3)} healing to others.")

        print("\nShielding Done:")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.total_shielded,3)} shield.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.amount_shielded_to_self,3)} shield to self.")
        print(f"{champion1.name} dealt {round(champion1.stat_tracker.amount_shielded_to_others,3)} shield to others.")

        print(f"{champion2.name} dealt {round(champion2.stat_tracker.total_shielded,3)} shield.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.amount_shielded_to_self,3)} shield to self.")
        print(f"{champion2.name} dealt {round(champion2.stat_tracker.amount_shielded_to_others,3)} shield to others.")
