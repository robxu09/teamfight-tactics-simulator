# main.py
import copy

from champions.champion_data import create_champions
from items.item_data import create_items
from scenarios.one_vs_one import OneVsOne

from scraper.scraper import get_html_content, extract_champion_urls, extract_champion_data, extract_items_data, export_items_to_csv, export_champion_details_to_csv

from helper_functions import print_formatted_dict


def main():

    # # items scraper 
    # url = 'https://tactics.tools/info/items'
    # html_content = get_html_content(url)
    # if html_content:
    #     items_data = extract_items_data(html_content)
    #     for item_data in items_data:
    #         print_formatted_dict(item_data)
    #         print()
    #     export_items_to_csv(items_data, "10", "test")

    # # champions scraper
    # url = 'https://lolchess.gg/champions/set10/'
    # html_content = get_html_content(url)
    # if html_content:
    #     champions_data = extract_champion_urls(html_content)

    # champs_data = []
    # for c in champions_data:
    #     url = 'https://lolchess.gg' + c[0]
    #     html_content = get_html_content(url)
    #     if html_content:
    #         champion_data = extract_champion_data(html_content, c[1])
    #         champs_data.append(champion_data)

    #     print_formatted_dict(champion_data)

    # export_champion_details_to_csv(champs_data, "10", "test")

    # Get a dictionary of Champion objects
    all_champions = create_champions(10, 'test')

    Tahm_Kench = all_champions.get("Tahm Kench_1")
    Vi = all_champions.get("Vi_1")
    
    Annie = all_champions.get("Annie_2")

    champion1 = Annie
    champion2 = Vi

    # Create items
    all_items = create_items(10, 'test')

    bt = all_items.get("Bloodthirster")

    # champion1.add_items(bt)
    champion2.add_items(bt)

    # Create and run the one versus one scenario
    one_vs_one_scenario = OneVsOne()
    one_vs_one_scenario.run(champion1, champion2, 50)


if __name__ == "__main__":
    main()