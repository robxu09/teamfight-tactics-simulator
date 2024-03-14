# scraper_module/scraper.py
import requests
import re
import sys
import json
from bs4 import BeautifulSoup

# https://lolchess.gg/champions/set10/
def get_html_content(url):
    headers = {'Accept-Language': 'en-US,en;q=0.9'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.content

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

def extract_champion_urls(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Assuming the HTML structure contains information about champions
    # Adjust these selectors based on the actual structure of the webpage
    champion_elements = soup.select('.css-xb1di8.e18qe9jt1 > *')

    champions_data = []
    c_data = ["",""]
    for champion_element in champion_elements:

        if champion_element:
            href_value = champion_element.get('href')
            if href_value:
                # print(href_value)
                c_data[0] = href_value

        if champion_element.name == 'span':
            # print(champion_element.text)
            c_data[1] = champion_element.text
            champions_data.append(c_data)
            c_data = ["",""]
    

    return champions_data

def extract_champion_data(html_content, champion_name):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Assuming the HTML structure contains information about champions
    # Adjust these selectors based on the actual structure of the webpage
    champion_data = {}

    champion_data['name'] = champion_name

    #scrape for cost and traits
    champion_elements = soup.select('div.css-14ved7i.e1eohesh3')
    if champion_elements:
        cost_html = champion_elements[0]
        traits_html = champion_elements[1:]

        if cost_html:
            # print(f"cost: {cost_html.text}")
            champion_data["cost"] = cost_html.text
        if traits_html:
            traits = []
            for trait_html in traits_html:
                traits.append(trait_html.text)
                # print(f"trait: {trait.text}")
            champion_data["traits"] = traits

#__next > div > div.css-1x48m3k.eetc6ox0 > div.content > div > section > div.css-17jx6qn.e1oq5z0y0 > div.css-j7qwjs.ed8e03y1 > article.css-0.ed8e03y0 > ul > li:nth-child(1) > div > p.css-1k9g2gq.e1ox7ks01
    champion_elements = soup.select('p.css-1k9g2gq.e1ox7ks01')
    if champion_elements:
        champion_data['health'] = champion_elements[0].text
        champion_data['attack damage'] = champion_elements[1].text


#__next > div > div.css-1x48m3k.eetc6ox0 > div.content > div > section > div.css-17jx6qn.e1oq5z0y0 > div.css-j7qwjs.ed8e03y1 > article.css-0.ed8e03y0 > ul > li:nth-child(5) > div > p.css-fd4500.e1ox7ks02
    champion_data['ability power'] = 100

    champion_elements = soup.select('p.css-fd4500.e1ox7ks02')
    if champion_elements:
        champion_data['attack speed'] = champion_elements[3].text
        champion_data['armor'] = champion_elements[4].text
        champion_data['magic resist'] = champion_elements[5].text


#__next > div > div.css-1x48m3k.eetc6ox0 > div.content > div > section > div.css-17jx6qn.e1oq5z0y0 > div.css-j7qwjs.ed8e03y1 > article.css-0.ed8e03y0 > ul > li:nth-child(4) > div
        #__next > div > div.css-1x48m3k.eetc6ox0 > div.content > div > section > div.css-17jx6qn.e1oq5z0y0 > div.css-j7qwjs.ed8e03y1 > article.css-0.ed8e03y0 > ul > li:nth-child(4) > div > img
    champion_elements = soup.select('li.css-125gcuq.e1ox7ks04 > * > img')
    if champion_elements:
        
        img = champion_elements[0].get('src')

        if img == "//cdn.dak.gg/tft/images2/tft/attack-distance/ico_attack_distance301.png":

            champion_data['attack range'] = "1"
        
        elif img == "//cdn.dak.gg/tft/images2/tft/attack-distance/ico_attack_distance302.png":

            champion_data['attack range'] = "2"
        
        else:

            champion_data['attack range'] = "3+"

#__next > div > div.css-1x48m3k.eetc6ox0 > div.content > div > section > div.css-17jx6qn.e1oq5z0y0 > div.css-j7qwjs.ed8e03y1 > article.css-0.ed8e03y0 > figure > figcaption > div.css-1jo0lz.emxgp8x1 > div
    champion_elements = soup.select('div.css-xi7lq2.emxgp8x2 > *')
    for champion_element in champion_elements:

        if champion_element.name == 'span':
            # print(champion_element.text)
            m = champion_element.text
            # print(f"mana: {m}")
            pattern = r'\d+'

            # Use re.findall to find all matches of the pattern in the input string
            matches = re.findall(pattern, m)

            if matches:
                # Convert the matches to integers
                numbers = [int(match) for match in matches]

                champion_data['starting mana'] = numbers[0]
                champion_data['mana to cast'] = numbers[1]
            else:
                champion_data['starting mana'] = 0
                champion_data['mana to cast'] = sys.maxsize


    champion_elements = soup.select('figcaption.css-x2fcwe.emxgp8x3 > *')
    champion_data['description'] = ""

    for champion_element in champion_elements:
        # if champion_element.name == "span" or champion_element.name == "strong" or champion_element.name == "p":
        # print(f"{champion_element.text}")
        text_line = champion_element.get_text(separator=' ')
        if not text_line.lower().startswith(".css-"):
            champion_data['description'] += text_line
            champion_data['description'] += "\n"
            # print(f"{champion_element.get_text(separator=' ')}")
        

    return champion_data

def extract_items_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    items_data = []

    item_elements = soup.select('div.p-4.rounded.text-white1.bg-bg')

    item_elements = [
        element for element in item_elements if len(list(element.descendants)) > 1
]

    for item in item_elements:

        item_data={}
        # get item name
        # print(tag_descendants[0])
        name=''
        first_string_descendant = next(item.strings, None)
        if first_string_descendant:
            name=first_string_descendant

        print(name)

        #get item stats
        item_stats=''
        stats = item.select('div.flex.flex-col.text-xs.text-white2')
        for stat in stats:
            item_stats = stat.get_text(separator=' ')
            print(item_stats)

        item_details=''
        details = item.select('div.leading-tight.text-sm.leading-tight')
        for det in details:
            item_details = det.get_text(separator=' ')
            print(item_details)

        item_data['name']=name
        item_data['stats']=stats
        item_data['description']=details

        items_data.append(item_data)

    return items_data