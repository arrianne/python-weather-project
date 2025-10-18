import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """

    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    # The fromisoformat() method in Python's datetime module is used to parse a string in ISO 8601 format and return a datetime object. This method provides a convenient way to convert standardized date and time strings into Python's native datetime objects. 
    iso_readable = datetime.fromisoformat(iso_string)

    # The strftime() method in Python's datetime module is used to format datetime objects into readable strings based on specified format codes.
    return iso_readable.strftime("%A %d %B %Y")




def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_fahrenheit = float(temp_in_fahrenheit) 

    # To convert Fahrenheit to Celsius, subtract 32 from the Fahrenheit temperature and then divide the result by 1.8
    temp_in_celsius = (temp_in_fahrenheit - 32) * 5.0 / 9.0

    # for 1 decimal place - rounded_number = round(number, 1)
    return round(temp_in_celsius, 1)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # Add up all the numbers and divide by how many numbers there are
    return sum(weather_data) / len(weather_data)

# example = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
# print(calculate_mean(example))  # Should return 30.0



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip header row - this was causing ValueError.
        data = [
            # Makes sure to convert temperature strings to integers
            [row[0], int(row[1]), int(row[2])]
            for row in reader
            # Skip empty or incomplete rows
            if row and len(row) >= 3
        ]
    return data



def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    # Guard clause handling empty list
    # If weather_data is empty (has no elements), then not weather_data is True.
    if not weather_data:
        return ()
    # find min value
    min_value = min(weather_data)

     # Find last index where min_value appears
    for num in range(len(weather_data) - 1, -1, -1):
        if weather_data[num] == min_value:
            return float(min_value), num  # Ensure value is float (per test expectation)


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    pass



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
