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

    if not weather_data:
        return 0.0  # Avoid ZeroDivisionError if list is empty
    
    # Convert all values to float
    numbers = [float(temp) for temp in weather_data]
    # Add up all the numbers and divide by how many numbers there are
    return sum(numbers) / len(numbers)
    

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
    
    # Convert all values to float for comparison
    temps_float = [float(value) for value in weather_data]

    # find min value
    min_value = min(temps_float)

    # Find last index where min_value appears
    for i in range(len(temps_float) - 1, -1, -1):
        if temps_float[i] == min_value:
            return (min_value), i


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if not weather_data:
        return ()
    
    # Convert all values to float for comparison
    temps_float = [float(value) for value in weather_data]

    max_value = max(temps_float)

    for num in range(len(temps_float) - 1, -1, -1):
        if temps_float[num] == max_value:
            return float(max_value), num  # Ensure value is float (per test expectation)




def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    if not weather_data:
        return "No weather data available.\n"

    num_days = len(weather_data)

    # Extract min and max temperatures directly (already in Celsius)
    min_temps = [convert_f_to_c(day[1]) for day in weather_data]
    max_temps = [convert_f_to_c(day[2]) for day in weather_data]

    # Find lowest and highest temps and their last positions
    min_temp, min_index = find_min(min_temps)
    max_temp, max_index = find_max(max_temps)

    # Get corresponding dates
    min_date = convert_date(weather_data[min_index][0])
    max_date = convert_date(weather_data[max_index][0])

    # Calculate averages
    avg_low = calculate_mean(min_temps)
    avg_high = calculate_mean(max_temps)

    # Build the summary string
    summary = (
        f"{num_days} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(min_temp)}, and will occur on {min_date}.\n"
        f"  The highest temperature will be {format_temperature(max_temp)}, and will occur on {max_date}.\n"
        f"  The average low this week is {format_temperature(round(avg_low, 1))}.\n"
        f"  The average high this week is {format_temperature(round(avg_high, 1))}.\n"
    )

    return summary

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return "No daily weather data available.\n"

    # Initializes an empty list to store the daily summaries.
    # We’ll build one string per day, then join them all at the end.
    summary_lines = []

    # Iterate over each day's data in the weather_data list.
    for day in weather_data:
        date = convert_date(day[0])
        min_c = format_temperature(convert_f_to_c(day[1]))
        max_c = format_temperature(convert_f_to_c(day[2]))

        daily_summary = (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_c}\n"
            f"  Maximum Temperature: {max_c}\n"
        )

        summary_lines.append(daily_summary)

    return "\n".join(summary_lines) + "\n"
