# main.py
import copy

from champions.champion_data import create_champions
from items.item_data import create_items
from scenarios.one_vs_one import OneVsOne

from simulation_system.simulator import scrape_champions_to_csv, scrape_items_to_csv, scrape_champions_and_items_to_csv


def main():

    while True:
        # Ask for console input
        user_input = input("Enter a command (type 'exit' to quit) (type 'help' for commands): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break  # Exit the loop

        if user_input.lower() == 'help':
            process_help()

        if user_input.lower() == 'scrapeci':
            process_scrape_champions_and_items_to_csv()

        if user_input.lower() == 'scrapec':
            process_scrape_champions_to_csv()

        if user_input.lower() == 'scrapei':
            process_scrape_items_to_csv()

    # main loop:
        # 1. can import champion data to csv
        # 2. can import item data to csv

        # 3. run a simulation
            # create all champions objects. create all items objects.
            # ask user to select from different types of simulation options available.
                # options include: 2 units fight. after being given items. (only option currently available)
                    # run simulation and print (export) results
    
        # 4. quit
    # end loop
    

    # # Get a dictionary of Champion objects
    # all_champions = create_champions(10, 'test')

    # Tahm_Kench = all_champions.get("Tahm Kench_1")
    # Vi = all_champions.get("Vi_1")
    
    # Annie = all_champions.get("Annie_2")

    # champion1 = Annie
    # champion2 = Vi

    # # Create items
    # all_items = create_items(10, 'test')

    # bt = all_items.get("Bloodthirster")

    # # champion1.add_items(bt)
    # champion2.add_items(bt)

    # # Create and run the one versus one scenario
    # one_vs_one_scenario = OneVsOne()
    # one_vs_one_scenario.run(champion1, champion2, 50)
            
def process_help():
    print("scrapeci: scrape champions and items data to csv")
    print("scrapec: scrape champions data to csv")
    print("scrapei: scrape items data to csv")

def process_scrape_champions_and_items_to_csv():
    user_input = input("Enter two text values separated by a space. [Set, Patch]: ")
    # Split the input into two separate values
    values = user_input.split()

    # Check if exactly two values were provided
    if len(values) != 2:
        print("Please enter exactly two text values separated by a space.")
    else:
        value1, value2 = values
        print(f"Scraping champions and items for Set {value1}, Patch {value2}.")
        scrape_champions_and_items_to_csv(value1, value2)

def process_scrape_champions_to_csv():
        user_input = input("Enter two text values separated by a space. [Set, Patch]: ")
        # Split the input into two separate values
        values = user_input.split()

        # Check if exactly two values were provided
        if len(values) != 2:
            print("Please enter exactly two text values separated by a space.")
        else:
            value1, value2 = values
            print(f"Scraping champions for Set {value1}, Patch {value2}.")
            scrape_champions_to_csv(value1, value2)

def process_scrape_items_to_csv():
        user_input = input("Enter two text values separated by a space. [Set, Patch]: ")
        # Split the input into two separate values
        values = user_input.split()

        # Check if exactly two values were provided
        if len(values) != 2:
            print("Please enter exactly two text values separated by a space.")
        else:
            # Process the user input (add your code here)
            value1, value2 = values
            print(f"Scraping items for Set {value1}, Patch {value2}.")
            scrape_items_to_csv(value1, value2)

if __name__ == "__main__":
    main()