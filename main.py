# main.py
import copy

from champions.champion_data import create_champions
from items.item_data import create_items
from scenarios.one_vs_one import OneVsOne

from scraper.scraper import get_html_content, extract_champion_urls, extract_champion_data



def main():

    #test scraper
    url = 'https://lolchess.gg/champions/set11/'
    html_content = get_html_content(url)
    if html_content:
        champions_data = extract_champion_urls(html_content)
    # for c in champions_data:
    #     print(f"{c[1]}: {c[0]}")

    for c in champions_data:
        url = 'https://lolchess.gg' + c[0]
        print(f'{c[1]}')
        html_content = get_html_content(url)
        if html_content:
            champion_data = extract_champion_data(html_content)
        print(f"cost: {champion_data['cost']}")
        print(f"traits: {champion_data['traits']}")
        print(f"health: {champion_data['health']}")
        print(f"attack damage: {champion_data['attack damage']}")
        print(f"ability power: {champion_data['ability power']}")
        print(f"attack speed: {champion_data['attack speed']}")
        print(f"armor: {champion_data['armor']}")
        print(f"magic resist: {champion_data['magic resist']}")
        print(f"attack range: {champion_data['attack range']}")
        print(f"starting mana: {champion_data['starting mana']}")
        print(f"mana to cast: {champion_data['mana to cast']}")
        print(f"dscription: \n{champion_data['description']}")
        print()

    # Get a dictionary of Champion objects
    all_champions = create_champions(10, 'test')

    Tahm_Kench = all_champions.get("Tahm Kench_1")
    Vi = all_champions.get("Vi_1")
    Annie = all_champions.get("Annie_2")

    champion1 = Annie
    champion2 = Vi

    # Create items
    all_items = create_items(10, 'test')

    # components
    chain_vest = all_items.get("Chain Vest")
    negatron_cloak = all_items.get("Negatron Cloak")

    bloodthirster = all_items.get("Bloodthirster")
    deathblade = all_items.get("Deathblade")
    infinity_edge = all_items.get("Infinity Edge")
    jeweled_gauntlet = all_items.get("Jeweled Gauntlet")
    last_whisperer = all_items.get("Last Whisperer")
    warmogs_armor = all_items.get("Warmog's Armor")

    # give items to champion 1
    # champion1.add_items(deathblade)
    champion1.add_items(bloodthirster)
    # champion1.add_items(last_whisperer)
    # champion1.add_items(infinity_edge)
    champion1.add_items(jeweled_gauntlet)
    champion1.add_items(warmogs_armor)
    # champion1.add_items(warmogs_armor)


    # give items to champion 2
    champion2.add_items(bloodthirster)
    # champion2.add_items(infinity_edge)
    # champion2.add_items(warmogs_armor)
    champion2.add_items(warmogs_armor)
    champion2.add_items(negatron_cloak)
    # champion2.add_items(warmogs_armor)
    # champion2.add_items(warmogs_armor)
    # champion2.add_items(chain_vest)

    # Create and run the one versus one scenario
    one_vs_one_scenario = OneVsOne()
    # one_vs_one_scenario.run(champion1, champion2, 50)


    # champion1.print_champion_items()
    # champion2.print_champion_items()

if __name__ == "__main__":
    main()