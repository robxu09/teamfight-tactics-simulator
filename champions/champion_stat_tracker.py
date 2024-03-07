# champion_data.py

class ChampionStatTracker:
    
    def __init__(self, champion):

        # champion
        self.champion = champion

        # Properties
        # Damage Done
        self.total_damage_done = 0
        self.ad_damage_done = 0
        self.ap_damage_done = 0
        self.true_damage_done = 0

        self.total_damage_done_to_target = 0
        self.ad_damage_done_to_target = 0
        self.ap_damage_done_to_target = 0
        self.true_damage_done_to_target = 0

        self.total_damage_done_to_others = 0
        self.ad_damage_done_to_others = 0
        self.ap_damage_done_to_others = 0
        self.true_damage_done_to_others = 0

        # Damage Taken
        self.total_damage_taken = 0

        # Healing Done
        self.amount_healed_to_self = 0
        self.amount_healed_to_others = 0
        self.total_healed = 0

        # Shielding Done
        self.amount_shielded_to_self = 0
        self.amount_shielded_to_others = 0
        self.total_shielded = 0

        # Time alive
        self.time_survived = 0

    # Function placeholders
    def update_stats(self):
        pass

    def update_damage_done(self, amount, damage_type, to_real_target):

        self.total_damage_done += amount
        if(to_real_target):
            self.total_damage_done_to_target += amount
        else:
            self.total_damage_done_to_others += amount


        if(damage_type == 'AD'):
            self.ad_damage_done += amount
            if(to_real_target):
                self.ad_damage_done_to_target += amount
            else:
                self.ad_damage_done_to_others += amount
        elif(damage_type == 'AP'):
            self.ap_damage_done += amount
            if(to_real_target):
                self.ap_damage_done_to_target += amount
            else:
                self.ap_damage_done_to_others += amount
        elif(damage_type == 'TRUE'):
            self.true_damage_done += amount
            if(to_real_target):
                self.true_damage_done_to_target += amount
            else:
                self.true_damage_done_to_others += amount

    def update_healing_done(self, amount, to_real_target):
        self.total_healed += amount
        if(to_real_target):
            self.amount_healed_to_self += amount
        else:
            self.amount_healed_to_others += amount

    def update_shielding_done(self, amount, to_real_target):
        self.total_shielded += amount
        if(to_real_target):
            self.amount_shielded_to_self += amount
        else:
            self.amount_shielded_to_others += amount

    def update_damage_taken(self, amount):

        self.total_damage_taken += amount

