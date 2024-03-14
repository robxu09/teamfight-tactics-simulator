# helper_functions.py

def count_decimal_places(number):
    # Convert the number to a string
    number_str = str(number)

    # Check if the number has a decimal point
    if '.' in number_str:
        # Find the index of the decimal point
        decimal_index = number_str.index('.')

        # Count the characters after the decimal point
        decimal_places = len(number_str) - decimal_index - 1
        return decimal_places
    else:
        # If there is no decimal point, return 0
        return 0


def print_formatted_dict(input_dict):
    if isinstance(input_dict, dict):
        for key, value in input_dict.items():

            if isinstance(value, dict):
                print(f"\n{key}: ")
                print_formatted_dict(value)
            else:
                print(f"{key}: {value}")
