# tests/test_champion.py
import pytest
from champions.champion import Champion
from champions.champion_data import create_champions

# champion fixture
@pytest.fixture
def test_champion():
    # Get a dictionary of Champion objects
    test_champion = Champion("Test Champion", health=10000, attack_damage=10, ability_power=20, 
                             armor=50, magic_resist=100, starting_mana=10, mana_to_cast=50, attack_speed=0.25)

    return test_champion

@pytest.fixture
def test_champion_2():
    # Get a dictionary of Champion objects
    test_champion_2 = Champion("Test Champion 2", health=10000, attack_damage=10, ability_power=20, 
                             armor=50, magic_resist=100, starting_mana=10, mana_to_cast=50, attack_speed=0.25)

    return test_champion_2

# champion creation
def test_champion_creation(test_champion):
    # Your test for champion creation goes here
    # Get a dictionary of Champion objects

    assert test_champion.health == 10000
    assert test_champion.attack_damage == 10
    assert test_champion.ability_power == 20
    assert test_champion.armor == 50
    assert test_champion.magic_resist == 100

    assert test_champion.critical_strike_chance == 0.25
    assert test_champion.critical_strike_damage == 1.4
    

# champion calculation functions

# Test case for calculate_bonus_critical_strike_damage
def test_calculate_bonus_critical_strike_damage(test_champion):

    test_champion.attack_damage = 10
    test_champion.critical_strike_chance = 0.25
    test_champion.critical_strike_damage = 1.4

    expected = 0.25*10*1.4 + 0.75*10 - 10

    assert test_champion.calculate_bonus_critical_strike_damage(test_champion.attack_damage) == expected

# Test case for calculate_armor_after_sunder
def test_calculate_armor_after_sunder(test_champion):

    test_champion.armor = 50
    test_champion.sunder_amount = 0.3

    armor_after_sunder = test_champion.calculate_armor_after_sunder()

    assert armor_after_sunder == (50 * (1-0.3))

# Test case for calculate_physical_damage_after_armor
def test_calculate_physical_damage_after_armor(test_champion, test_champion_2):

    initial_damage = 11

    test_champion_2.armor = 50
    test_champion_2.sunder_amount = 0.3
    test_champion_2.armor_after_sunder = test_champion_2.calculate_armor_after_sunder()

    expected = 11 * (1-((50 * (1-0.3))/(100+(50 * (1-0.3)))))

    assert test_champion.calculate_physical_damage_after_armor(initial_damage, test_champion_2) == expected

# Test case for calculate_total_attack_damage_done
def test_calculate_total_attack_damage_done(test_champion, test_champion_2):

    # ad = 10. armor = 50. crit% =0.25 crit dmg = 1.4. bonus damage = 0. bonus resist = 0.
    # (0.75 * 10 + 0.25 * 10 * 1.4) * (50 / 100+50)
    #  7.5 + 
    test_champion.attack_damage = 10
    test_champion.critical_strike_chance = 0.25
    test_champion.critical_strike_damage = 1.4

    test_champion_2.armor = 50
    test_champion_2.sunder_amount = 0.3
    test_champion_2.armor_after_sunder = test_champion_2.calculate_armor_after_sunder()

    expected = (0.25*10*1.4 + 0.75*10) * (1-((50 * (1-0.3))/(100+(50 * (1-0.3)))))

    assert test_champion.calculate_total_attack_damage_done(test_champion.attack_damage, test_champion_2, True) == expected

# Test case for calculate_magic_resist_after_shred
def test_calculate_magic_resist_after_shred(test_champion):

    test_champion.magic_resist = 100
    test_champion.shred_amount = 0.3

    magic_resist_after_shred = test_champion.calculate_magic_resist_after_shred()

    assert magic_resist_after_shred == (100 * (1-0.3))

# Test case for calculate_magic_damage_after_magic_resist
def test_calculate_magic_damage_after_magic_resist(test_champion, test_champion_2):
    initial_damage = 20

    test_champion_2.magic_resist = 100
    test_champion_2.shred_amount = 0.3
    test_champion_2.magic_resist_after_shred = test_champion_2.calculate_magic_resist_after_shred()

    expected = 20 * (1-((100 * (1-0.3))/(100+(100 * (1-0.3)))))

    assert test_champion.calculate_magic_damage_after_magic_resist(initial_damage, test_champion_2) == expected

# Test case for calculate_total_magic_damage_done without crit
def test_calculate_total_magic_damage_done_without_crit(test_champion, test_champion_2):
    test_champion.ability_power = 20
    test_champion.critical_strike_chance = 0.25
    test_champion.critical_strike_damage = 1.4

    test_champion_2.magic_resist = 100
    test_champion_2.shred_amount = 0.3
    test_champion_2.magic_resist_after_shred = test_champion_2.calculate_magic_resist_after_shred()

    expected = 20 * (1-((100 * (1-0.3))/(100+(100 * (1-0.3)))))

    assert test_champion.calculate_total_magic_damage_done(test_champion.ability_power, test_champion_2, False) == expected

# Test case for calculate_total_magic_damage_done with crit
def test_calculate_total_magic_damage_done_with_crit(test_champion, test_champion_2):
    test_champion.ability_power = 20
    test_champion.critical_strike_chance = 0.25
    test_champion.critical_strike_damage = 1.4

    test_champion.can_crit_ult = True

    test_champion_2.magic_resist = 100
    test_champion_2.shred_amount = 0.3
    test_champion_2.magic_resist_after_shred = test_champion_2.calculate_magic_resist_after_shred()

    expected = (0.25*20*1.4 + 0.75*20) * (1-((100 * (1-0.3))/(100+(100 * (1-0.3)))))

    assert test_champion.calculate_total_magic_damage_done(test_champion.ability_power, test_champion_2, True) == expected




# champion main actions

