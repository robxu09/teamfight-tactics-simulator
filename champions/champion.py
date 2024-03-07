# entities/champion.py
import copy

from constants import SIMULATION_TICK_SPEED, SIMULATION_TICK_SPEED_DECIMALS

from simulation_system.simulation_steps import Simulation_Step
from champions.champion_stat_tracker import ChampionStatTracker

class Champion:
    def __init__(self, name, star_level=1, health=0, attack_damage=0, ability_power=0, armor=0,
                 magic_resist=0, starting_mana=0, mana_to_cast=0, attack_speed=0, attack_range=0, traits = [], description=""):
        
        self.name = name
        self.star_level = star_level
        self.traits = traits

        self.stat_tracker = ChampionStatTracker(self)

        # EFFECTS

        # effects gets added on creation. defined elsewhere
        self.effects = []
        self.description = description

        # real time effect data
        self.amt_of_times_effects_triggered = []
        self.most_recent_effects_cast_time = []
        
        self.amt_of_times_ultimate_triggered = 0
        self.most_recent_ultimate_cast_time = -1


        # CHAMPION STATS

        # original stats to keep track of
        self.original_attack_damage = attack_damage
        self.original_attack_speed = attack_speed
        self.original_total_health = health
        self.can_crit_ult_default = False

        # basic combat stats
        self.total_health = health
        self.attack_damage = attack_damage
        self.ability_power = ability_power
        self.armor = armor
        self.magic_resist = magic_resist
        self.starting_mana = starting_mana
        self.mana_to_cast = mana_to_cast
        self.attack_speed = attack_speed
        self.critical_strike_chance = 0.25
        self.critical_strike_damage = 1.4
        self.attack_range = attack_range

        self.outgoing_damage_amp_percentage = 0
        self.incoming_damage_reduction_percentage = 0

        # debuff stats
        self.burn_amount = 0
        self.wound_amount = 0
        self.shred_amount = 0
        self.sunder_amount = 0

        # extra combat stats 
        self.omnivamp = 0
        self.shield = 0
        self.mana_gained_on_hit = 1
        self.mana_gained_on_attack = 10
        self.health = self.total_health
        self.armor_after_sunder = self.armor * (1 - self.sunder_amount)
        self.magic_resist_after_shred = self.magic_resist * (1 - self.shred_amount)
        self.can_crit_ult = self.can_crit_ult_default

        # ITEMS

        # items
        self.items = []

        # TIMER

        # timer details
        self.timer = None

        # FUNCTIONAL COMBAT STATUS DETAILS

        self.can_cast_ultimate = False
        self.stun_time = 0
        self.burn_time = 0
        self.attack_wait_timer = 0
        self.mana = self.starting_mana
        self.is_casting_ultimate = False
        self.is_mana_locked = False


        # COMBAT ANALYSIS DATA

        # real time combat stats
        self.ultimate_damage_done = 0
        self.amount_healed = 0

        # combat data
        self.autoattack_damage_done = 0
        self.amount_damage_taken = 0

        print(f"{self.name} has been created.")

    # CHAMPION MAIN ACTIONS to be performed in simulation loop

    # each champion must check and update status at start of every iteration of simulation
    def update_status_start(self, enemy_champion):

        # check if can cast ultimate
        self.can_cast_ultimate = True if self.mana >= self.mana_to_cast else False

        # update current armor and mr after sunder and shred
        self.armor_after_sunder = self.calculate_armor_after_sunder()
        # print(f"{self.name} armor_after_sunder: {self.armor_after_sunder}")
        self.magic_resist_after_shred = self.calculate_magic_resist_after_shred()
        
        # activate relevant effects
        self.activate_effects(Simulation_Step.OnStartStatusUpdate, enemy_champion, [])

        # apply burn damage
        if(self.burn_amount > 0 and (self.timer.current_time) % (1 / SIMULATION_TICK_SPEED) == 0):
            enemy_champion.deal_burn_damage(self)

    # each champion must check and update status at end of every iteration of simulation
    # handles wiping of effects
    def update_status_end(self, enemy_champion):

        # check if can cast ultimate
        self.can_cast_ultimate = True if self.mana >= self.mana_to_cast else False

        # update current armor and mr after sunder and shred
        self.armor_after_sunder = self.calculate_armor_after_sunder()
        self.magic_resist_after_shred = self.calculate_magic_resist_after_shred()

        # tick down stun time
        if(self.stun_time > 0):
            self.stun_time -= SIMULATION_TICK_SPEED
        else:
            self.stun_time = 0

        # receive burn damage
        if(self.burn_time > 0 and round(self.burn_time, SIMULATION_TICK_SPEED_DECIMALS) % 1 == 0):
            self.take_burn_damage()

        # tick down burn time
        if(self.burn_time > 0):
            self.burn_time -= SIMULATION_TICK_SPEED
        else:
            self.burn_time = 0
        
        self.activate_effects(Simulation_Step.OnEndStatusUpdate, enemy_champion, [])

    def autoattack_if_possible(self, target):
        # can't attack if conditions
        if (self.is_casting_ultimate == False and self.stun_time <= 0):
            # wait for ability to attack
            if(self.attack_wait_timer >= (1 / self.attack_speed)):

                # execute auto attack
                self.execute_auto_attack(target)

                # reset attack timer
                self.attack_wait_timer = 0

            self.attack_wait_timer += SIMULATION_TICK_SPEED

    def execute_auto_attack(self, target):
        # activate any effects that happen On Autoattack
        self.activate_effects(Simulation_Step.BeforeAutoAttack, target, [])


        # base AD with average crit bonus against opponent armor
        AD_attack_amount = self.calculate_total_attack_damage_done(self.attack_damage, target, True)

        self.deal_damage(target, AD_attack_amount, "AD")

        # after autoattacking, give yourself mana
        self.gain_mana(self.mana_gained_on_attack)

        # activate any effects that happen On Autoattack
        self.activate_effects(Simulation_Step.OnAutoAttack, target, [AD_attack_amount, "AD"])

    def cast_ultimate_if_possible(self, target):
        
        if (self.stun_time <= 0):
            #check if ultimate is castable
            if(self.can_cast_ultimate):
                # Implement the logic for casting an ultimate
                # print(f"{self.name} casts their ultimate against {target.name}!")

                self.activate_effects(Simulation_Step.OnCastUltimate, target, [])


                self.can_cast_ultimate = False

                self.mana = 0

    # BASIC CHAMPION ACTIONS  

    # damage_type = "AD", "AP", "TRUE"

    def deal_damage(self, target, amount, damage_type):

        self.activate_effects(Simulation_Step.BeforeDealDamage, target, [amount, damage_type])

        amount *= (self.outgoing_damage_amp_percentage+1) * (target.incoming_damage_reduction_percentage+1)

        print(f"{self.name} deals {round(amount,3)} damage to {target.name}!")
        target.take_damage(amount)

        # apply omnivamp
        self.apply_omnivamp(amount)

        # when you deal damage to an opponent, give them mana
        target.set_mana(target.mana + target.mana_gained_on_hit)

        # activate bonus effects after dealing damage. extra damage is added as bonus damage
        # fire extra bolt of damage, increase damage, etc.
        # on deal damage, extra input = damage amount
        self.activate_effects(Simulation_Step.OnDealDamage, target, [amount, damage_type])

    # dealing bonus damage. (does not count as a hit. it's extra damage from a previous hit)
    
    # damage_type = "AD", "AP", "TRUE"

    def deal_bonus_damage(self, target, amount, damage_type):
        self.activate_effects(Simulation_Step.BeforeDealBonusDamage, target, [amount, damage_type])
        amount *= (self.outgoing_damage_amp_percentage+1) * (target.incoming_damage_reduction_percentage+1)

        target.take_damage(amount)
        # print(f"{self.name} deals {round(amount,3)} damage to {target.name}!")

        # apply omnivamp
        self.apply_omnivamp(amount)

    def deal_healing(self, target, amount):
        self.activate_effects(Simulation_Step.BeforeDealHealing, target, [amount])
        target.heal(amount)
        self.activate_effects(Simulation_Step.OnDealHealing, target, [amount])
        # print(f"{self.name} heals {target.name} for {round(amount,3)} health!")
    
    def take_burn_damage(self):
        self.take_damage(self.burn_amount * self.total_health * (1+self.incoming_damage_reduction_percentage))

    def take_damage(self, amount):

        # first, take damage to shield
        self.shield = self.shield - amount
        if(self.shield < 0):
            amount = -1 * self.shield
            self.shield = 0
        else:
            amount = 0
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print(f"{self.name} takes {round(amount,3)} damage!")

    def heal(self, amount):
        amount = amount * (1-self.wound_amount)
        self.health += amount
        # print(f"{self.name} is healed for {round(amount,3)} health!")

    def apply_omnivamp(self, amount):
        self.heal(amount*self.omnivamp)

    def become_burned(self, amount, time):
        self.burn_amount = amount
        self.burn_time = time
        # print(f"get burned {self.burn_time}")

    def become_sundered(self, amount):
        self.sunder_amount = amount

    def become_shredded(self, amount):
        self.shred_amount = amount

    def become_wounded(self, amount):
        self.wound_amount = amount

    def gain_mana(self, amount):
        if(self.is_mana_locked == False):
            self.set_mana(self.mana + amount)

    # EFFECTS ACTIVATOR (effects handle if it is the right simulation step for themselves)

    # activates on all Simulation phase triggers
    # handles calling effects of champion, champion's items, champion's augments, champion's traits
            
    # data is a list []
    # dealing damage simulation steps: [amount, damage_type]
    # dealing other stats: [amount]
    # other phases: []
    def activate_effects(self, simulation_step, enemy_champion, data):
        # active personal effects
        self.activate_personal_effects(simulation_step, self, enemy_champion, data)

        # activate item effects
        for item in self.items:

            item.give_base_stats(simulation_step, self)
            item.activate_effect(simulation_step, self, enemy_champion, self.timer.current_time, data)

        # activate augment effects

        # active other effects
        
    # ACTIVATE CHAMPION EFFECTS HELPER

    def activate_personal_effects(self, simulation_step, champion, enemy_champion, damage):

        for effect in self.effects:
            if effect:
                e = effect[0]
                did_trigger, when_triggered =  e()(simulation_step, champion, enemy_champion, self.timer.current_time, damage, effect[1], effect[2])
                # didtrigger: 1 -> start trigger, 0 -> no trigger, -1 -> end trigger
                # triggertime: time of start-trigger. on end/no trigger set back to -1
                if (did_trigger != -1):
                    effect[1] += did_trigger
                    # print(f"did_trigger {effect[1]}")
                if (did_trigger == 1 or did_trigger == -1):
                    effect[2] = when_triggered
                    # print(f"when_triggered {effect[2]}")

    # HELPER CALCULATIONS

    # helper functions for calculating total AD damage
    # base AD with average crit bonus against opponent armor
    def calculate_total_attack_damage_done(self, damage, target, can_crit=False):
        AD_attack_amount = damage
        if can_crit:
            AD_attack_amount += self.calculate_bonus_critical_strike_damage(AD_attack_amount)
        AD_attack_amount = self.calculate_physical_damage_after_armor(AD_attack_amount, target)
        return AD_attack_amount
    
        # helper functions for calculating total AD damage
    # base AD with average crit bonus against opponent armor
    def calculate_total_magic_damage_done(self, damage, target, can_crit=False):
        AP_attack_amount = damage
        if can_crit:
            AP_attack_amount += self.calculate_bonus_critical_strike_damage(AP_attack_amount)
        AP_attack_amount = self.calculate_magic_damage_after_magic_resist(AP_attack_amount, target)
        return AP_attack_amount

    # helper functions for calculating damage after resistances
    def calculate_physical_damage_after_armor(self, damage, enemy_champion):
        return damage * (1 - (enemy_champion.armor/(enemy_champion.armor + 100)))
    
    def calculate_magic_damage_after_magic_resist(self, damage, enemy_champion):
        return damage * (1 - (enemy_champion.magic_resist/(enemy_champion.magic_resist + 100)))
    
    # helper function for calculating bonus critical strike damage
    def calculate_bonus_critical_strike_damage(self, amount):
        # (probability crit * base-with-crit damage + probability no crit + base damage) - base damage = average bonus damage. (without the base damage)
        return (self.critical_strike_chance * (self.critical_strike_damage * amount) + (1 - self.critical_strike_chance) * amount) - amount
    
    def calculate_armor_after_sunder(self):
        return self.armor * (1-self.sunder_amount)

    def calculate_magic_resist_after_shred(self):
        return self.magic_resist * (1-self.shred_amount)
    
    # SETTERS

    # SET EFFECTS

    # set effect ability for each champion (not ultimate ability)
    def set_effects(self, custom_effects):

        c = custom_effects()

        for effect in c:
            self.effects.append([effect, 0, -1])

    # SET ITEMS for CHAMPION

    def add_items(self, item):

        self.items.append(copy.deepcopy(item))
        # print(f"{self.name} equipped a(n) {item.name}.")

    # CHAMPION STAT SETTERS

    # setters that require more than just changing the value
    def set_attack_speed(self, amount):
        self.attack_speed = min(amount, 5.0)
        # print(f"atk speed {self.attack_speed}")
    
    def set_armor(self, amount):
        if(amount < 0):
            self.armor = 0
        else:
            self.armor = amount

    def set_magic_resist(self, amount):
        if(amount < 0):
            self.magic_resist = 0
        else:
            self.magic_resist = amount

    def set_sunder_amount(self, amount):
        if(amount >= 1):
            self.sunder_amount = 1
        else:
            self.sunder_amount = amount

    def set_shred_amount(self, amount):
        if(amount >= 1):
            self.shred_amount = 1
        else:
            self.shred_amount = amount

    def set_stun_time(self, amount):
        self.stun_time = max(amount, self.stun_time)

    def set_critical_strike_chance(self, amount):
        if(amount >= 1.0):
            self.critical_strike_chance = 1.0
            bonus_crit_dmg = (amount - 1) / 2
            self.critical_strike_damage += bonus_crit_dmg
        else:
            self.critical_strike_chance = amount

    def set_mana(self, amount):
        self.mana = amount
        if(amount >= self.mana_to_cast):
            # turn on can cast ultimate trigger
            # print(f"{self.name} can cast ultimate. Current mana: {self.mana}. Mana to Cast: {self.mana_to_cast}")
            self.can_cast_ultimate = True


    # INFORMATION LOGGERS
    def print_champion_items(self):

        print(f"{self.name}'s items:")
        for item in self.items:
            print(f"{item.name}")
        print("\n")
