# scraper_module/scraper.py
import requests
from bs4 import BeautifulSoup

# https://lolchess.gg/champions/set10/
def get_html_content(url):
    headers = {'Accept-Language': 'en-US,en;q=0.9'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.content

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

def extract_champion_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Assuming the HTML structure contains information about champions
    # Adjust these selectors based on the actual structure of the webpage
    champion_elements = soup.select('.css-xb1di8.e18qe9jt1 > *')

    champions_data = []
    for champion_element in champion_elements:

        if champion_element:
            href_value = champion_element.get('href')
            if href_value:
                print(href_value)

        if champion_element.name == 'span':
            print(champion_element.text)

    return champions_data
