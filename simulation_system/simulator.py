import copy

from scraper.scraper import get_html_content, extract_champion_urls, extract_champion_data, extract_items_data, export_items_to_csv, export_champion_details_to_csv
from helper_functions import print_formatted_dict
from champions.champion_data import create_champions
from items.item_data import create_items

from scenarios.one_vs_one import OneVsOne


def run_1v1_with_two_champions(set, patch):


    # Get a dictionary of Champion objects
    all_champions = create_champions(set, patch)
    # Create items
    all_items = create_items(set, patch)

    print("One vs One: ")

    # create champion 1
    while True:
        user_input = input("Enter name of champion 1 (ie. 'Champion Name_3'): ")
        champion1 = copy.deepcopy(all_champions.get(user_input))
        if champion1:
            break
        else:
            print("invalid champion name")

    while True:
        user_input = input(f"Enter name of item to give to {champion1.name}. Enter N to stop adding items: ")
        item = copy.deepcopy(all_items.get(user_input))
        if user_input.lower() == "n":
            print("Done adding items")
            break
        elif item:
            champion1.add_items(item)
            print(f"Gave {champion1.name} one {item.name}.")
        else:
            print("invalid item name")
    
    # create champion 2
    while True:
        user_input = input("Enter name of champion 2 (ie. 'Champion Name_3'): ")
        champion2 = copy.deepcopy(all_champions.get(user_input))
        if champion2:
            break
        else:
            print("invalid champion name")


    while True:
        user_input = input(f"Enter name of item to give to {champion2.name}. Enter N to stop adding items: ")
        item = copy.deepcopy(all_items.get(user_input))
        if user_input.lower() == "n":
            print("Done adding items")
            break
        elif item:
            champion2.add_items(item)
            print(f"Gave {champion2.name} one {item.name}.")
        else:
            print("invalid item name")

    # Create and run the one versus one scenario
    one_vs_one_scenario = OneVsOne()
    results = one_vs_one_scenario.run(champion1, champion2, 50)
    print_results(results)

    return


def print_results(results):
    print_formatted_dict(results)

def scrape_champions_and_items_to_csv(set, patch):
    scrape_champions_to_csv(set, patch)
    scrape_items_to_csv(set, patch)

def scrape_champions_to_csv(set, patch):
    # champions scraper.  give set and patch
    url = 'https://lolchess.gg/champions/set' + set + '/'
    html_content = get_html_content(url)
    if html_content:
        champions_data = extract_champion_urls(html_content)

    champs_data = []
    for c in champions_data:
        url = 'https://lolchess.gg' + c[0]
        html_content = get_html_content(url)
        if html_content:
            champion_data = extract_champion_data(html_content, c[1])
            champs_data.append(champion_data)

        print_formatted_dict(champion_data)

    export_champion_details_to_csv(champs_data, set, patch)
    # end champions scraper function. end result is csv is generated

def scrape_items_to_csv(set, patch):
    # items scraper. give set and patch
    url = 'https://tactics.tools/info/items'
    html_content = get_html_content(url)
    if html_content:
        items_data = extract_items_data(html_content)
        for item_data in items_data:
            print_formatted_dict(item_data)
            print()
        export_items_to_csv(items_data, set, patch)
    # end items scraper function. end result is csv is generated
        
