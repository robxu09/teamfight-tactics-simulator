# entities/item.py

from simulation_system.simulation_steps import Simulation_Step

class Item:
    def __init__(self, name, bonus_attack_damage=0, bonus_ability_power=0,
                 bonus_magic_resist=0, bonus_armor=0, bonus_health=0, bonus_starting_mana=0,
                 bonus_attack_speed=0, bonus_critical_strike_chance=0.0, bonus_critical_strike_damage=0, 
                 bonus_attack_range=0, bonus_omnivamp=0, description=""):
        
        self.effect_implement = False

        self.name = name
        self.description = ""

        # bonus stats
        self.bonus_attack_damage = bonus_attack_damage
        self.bonus_ability_power = bonus_ability_power
        self.bonus_magic_resist = bonus_magic_resist
        self.bonus_armor = bonus_armor
        self.bonus_health = bonus_health
        self.bonus_starting_mana = bonus_starting_mana
        self.bonus_attack_speed = bonus_attack_speed
        self.bonus_critical_strike_chance = bonus_critical_strike_chance
        self.bonus_critical_strike_damage = bonus_critical_strike_damage
        self.bonus_attack_range = bonus_attack_range
        self.bonus_omnivamp = bonus_omnivamp

        # effect gets added on creation. defined elsewhere
        self.effects = []

        # realtime combat stats
        self.amt_of_times_effects_triggered = []
        self.most_recent_effects_cast_time = []

    def set_effects(self, custom_effects):
        
        c = custom_effects()

        for effect in c:
            self.effects.append([effect, 0, -1])
        
    def activate_effect(self, simulation_step, champion, enemy_champion, current_simulation_time, damage):

        for effect in self.effects:
            if effect:
                e = effect[0]
                did_trigger, when_triggered =  e()(simulation_step, champion, enemy_champion, self, current_simulation_time, damage, effect[1], effect[2])
                # didtrigger: 1 -> start trigger, 0 -> no trigger, -1 -> end trigger
                # triggertime: time of start-trigger. on end/no trigger set back to -1
                if (did_trigger != -1):
                    effect[1] += did_trigger
                if (did_trigger == 1 or did_trigger == -1):
                    effect[2] = when_triggered


    def give_base_stats(self, simulation_step, champion):

        if(simulation_step == Simulation_Step.OnInitiation):
            champion.attack_damage += self.bonus_attack_damage * champion.original_attack_damage * 0.01
            champion.ability_power += self.bonus_ability_power
            champion.set_magic_resist(champion.magic_resist + self.bonus_magic_resist)
            champion.set_armor(champion.armor + self.bonus_armor)
            champion.health += self.bonus_health
            champion.max_health += self.bonus_health
            champion.starting_mana += self.bonus_starting_mana
            champion.mana += self.bonus_starting_mana
            champion.set_attack_speed(champion.attack_speed + (self.bonus_attack_speed * 0.01 * champion.original_attack_speed))
            champion.set_critical_strike_chance(champion.critical_strike_chance + self.bonus_critical_strike_chance)
            champion.critical_strike_damage += self.bonus_critical_strike_damage
            # champion.attack_range += self.bonus_attack_range
            champion.omnivamp += self.bonus_omnivamp