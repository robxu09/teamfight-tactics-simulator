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

    # assert test_champion.calculate_bonus_critical_strike_damage(test_champion.attack_damage) == 0.25*10*1.4 + 0.75*10
    pass

# Test case for calculate_physical_damage_after_armor
def test_calculate_physical_damage_after_armor():
    pass

# Test case for calculate_total_attack_damage_done
def test_calculate_total_attack_damage_done(test_champion, test_champion_2):

    # ad = 10. armor = 50. crit% =0.25 crit dmg = 1.4. bonus damage = 0. bonus resist = 0.
    # (0.75 * 10 + 0.25 * 10 * 1.4) * (50 / 100+50)
    #  7.5 + 
    AD_attack_amount = round(test_champion.calculate_total_attack_damage_done(test_champion.attack_damage, test_champion_2, True),3)

    # assert AD_attack_amount != 3.667
    pass

# Test case for calculate_total_magic_damage_done
def test_calculate_total_magic_damage_done():
    pass

# Test case for calculate_magic_damage_after_magic_resist
def test_calculate_magic_damage_after_magic_resist():
    pass

# Test case for calculate_armor_after_sunder
def test_calculate_armor_after_sunder():
    pass

# Test case for calculate_magic_resist_after_shred
def test_calculate_magic_resist_after_shred():
    pass

# champion main actions

