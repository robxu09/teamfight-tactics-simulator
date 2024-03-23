from constants import SIMULATION_TICK_SPEED, DIGITS_TO_ROUND_TO
from helper_functions import print_formatted_dict

class SimulationResults:
    def __init__(self, champions, timer):

        self.champions = champions
        self.timer = timer

        # results is a dictionary: key = integer, value = Champion_results
        self.results = {}

    def populate_results(self):

        # for each champion, populate the dictionary with
        for index, champion in enumerate(self.champions, 1):
            self.results['Champion '+str(index)] = self.get_champion_results(champion)

    def get_simulation_runtime(self):

        return self.timer.current_time

    def get_champion_results(self, champion):

        item_names = []

        for item in champion.items:

            item_names.append(item.name)
        

        return {
            'name' : champion.name,
            'star_level' : champion.star_level,
            'time_survived': self.get_simulation_runtime(),
            'current_health' : round(champion.health, DIGITS_TO_ROUND_TO),

            'items' : item_names,
            
            'total_damage_done': round(champion.stat_tracker.total_damage_done, DIGITS_TO_ROUND_TO),
            'ad_damage_done': round(champion.stat_tracker.ad_damage_done, DIGITS_TO_ROUND_TO),
            'ap_damage_done': round(champion.stat_tracker.ap_damage_done, DIGITS_TO_ROUND_TO),
            'true_damage_done': round(champion.stat_tracker.true_damage_done, DIGITS_TO_ROUND_TO),

            'total_damage_done_to_target': round(champion.stat_tracker.total_damage_done_to_target, DIGITS_TO_ROUND_TO),
            'ad_damage_done_to_target': round(champion.stat_tracker.ad_damage_done_to_target, DIGITS_TO_ROUND_TO),
            'ap_damage_done_to_target': round(champion.stat_tracker.ap_damage_done_to_target, DIGITS_TO_ROUND_TO),
            'true_damage_done_to_target': round(champion.stat_tracker.true_damage_done_to_target, DIGITS_TO_ROUND_TO),

            'total_damage_done_to_others': round(champion.stat_tracker.total_damage_done_to_others, DIGITS_TO_ROUND_TO),
            'ad_damage_done_to_others': round(champion.stat_tracker.ad_damage_done_to_others, DIGITS_TO_ROUND_TO),
            'ap_damage_done_to_others': round(champion.stat_tracker.ap_damage_done_to_others, DIGITS_TO_ROUND_TO),
            'true_damage_done_to_others': round(champion.stat_tracker.true_damage_done_to_others, DIGITS_TO_ROUND_TO),

            'total_damage_taken': round(champion.stat_tracker.total_damage_taken, DIGITS_TO_ROUND_TO),

            'amount_healed_to_self': round(champion.stat_tracker.amount_healed_to_self, DIGITS_TO_ROUND_TO),
            'amount_healed_to_others': round(champion.stat_tracker.amount_healed_to_others, DIGITS_TO_ROUND_TO),
            'total_healed': round(champion.stat_tracker.total_healed, DIGITS_TO_ROUND_TO),

            'amount_shielded_to_self': round(champion.stat_tracker.amount_shielded_to_self, DIGITS_TO_ROUND_TO),
            'amount_shielded_to_others': round(champion.stat_tracker.amount_shielded_to_others, DIGITS_TO_ROUND_TO),
            'total_shielded': round(champion.stat_tracker.total_shielded, DIGITS_TO_ROUND_TO),

        }

