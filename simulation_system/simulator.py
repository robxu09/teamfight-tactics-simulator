from scraper.scraper import get_html_content, extract_champion_urls, extract_champion_data, extract_items_data, export_items_to_csv, export_champion_details_to_csv
from helper_functions import print_formatted_dict

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