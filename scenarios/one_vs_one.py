# entities/one_vs_one.py

# import numpy as np

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

        self.sim_results = SimulationResults([champion1, champion2], timer)
        self.sim_results.populate_results()
        # self.sim_results.print_results()
        return self.sim_results.results

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