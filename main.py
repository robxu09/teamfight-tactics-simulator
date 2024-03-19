# main.py
import copy

from simulation_system.simulator import scrape_champions_to_csv, scrape_items_to_csv, scrape_champions_and_items_to_csv, run_1v1_with_two_champions


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

        if user_input.lower() == 'runsim':
            process_run_simulator()
    
            
def process_help():
    print("scrapeci: scrape champions and items data to csv")
    print("scrapec: scrape champions data to csv")
    print("scrapei: scrape items data to csv")
    print("runsim: run simulation")

def process_run_simulator():
    user_input = input("Enter two text values separated by a space. [Set, Patch]: ")
    # Split the input into two separate values
    values = user_input.split()

    # Check if exactly two values were provided
    if len(values) != 2:
        print("Please enter exactly two text values separated by a space.")
    else:
        value1, value2 = values
        print(f"Scraping champions and items for Set {value1}, Patch {value2}.")
        run_1v1_with_two_champions(value1, value2)


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