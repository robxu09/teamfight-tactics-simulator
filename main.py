# main.py
import copy

from champions.champion_data import create_champions
from items.item_data import create_items
from scenarios.one_vs_one import OneVsOne



def main():

    # Get a dictionary of Champion objects
    all_champions = create_champions()

    Tahm_Kench = all_champions.get("Tahm Kench")
    Vi = all_champions.get("Vi")
    Annie = all_champions.get("Annie")

    champion1 = Annie
    champion2 = Vi

    # Create items
    all_items = create_items()

    Deathblade = all_items.get("Deathblade")
    Bloodthirster = all_items.get("Bloodthirster")
    Warmogs = all_items.get("Warmog's Armor")
    ChainVest = all_items.get("Chain Vest")
    LastWhisperer = all_items.get("Last Whisperer")

    # give items to champion 1
    # champion1.add_items(Deathblade)
    # champion1.add_items(Bloodthirster)
    # champion1.add_items(LastWhisperer)

    # give items to champion 2
    # champion2.add_items(Warmogs)
    # champion2.add_items(Warmogs)
    # champion2.add_items(Warmogs)
    # champion2.add_items(Warmogs)
    # champion2.add_items(ChainVest)

    # Create and run the one versus one scenario
    one_vs_one_scenario = OneVsOne()
    one_vs_one_scenario.run(champion1, champion2, 40)


    # champion1.print_champion_items()
    # champion2.print_champion_items()

if __name__ == "__main__":
    main()