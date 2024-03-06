from constants import SIMULATION_TICK_SPEED

class SimulationTimer:
    def __init__(self, start_time=0, end_time=0):
        self.start_time = start_time
        self.current_time = start_time
        self.end_time = end_time

    def increment_timer(self):
        self.current_time += SIMULATION_TICK_SPEED

    def print_current_time(self):
        print(f"Current Simulation Time: {self.current_time, 2}")