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

    # The fromisoformat() method in Python's datetime module formats datetime objects into strings using specific format codes
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

    # round() is a built-in Python function that rounds a number to a specified number of decimal places
    # 1 tells Python to round the number to 1 decimal place
    return round(temp_in_celsius, 1)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    # Got a ZeroDivisionError because list was empty so gave it a 0.0 float in this case.
    if not weather_data:
        return 0.0  
    
    # Convert all values to float as we look through the weather_data list
    # Uses list comprehension - quick way to build a new list in one line which is assigns to 'numbers'
    numbers = [float(temp) for temp in weather_data]
    # Add up all the numbers and divide by how many numbers there are
    return sum(numbers) / len(numbers)
    
# # Testing calculate_mean function
# example = [51.0, 58.2, 59.9, 52.4, 52.1, 48.4, 47.8, 53.43]
# print(calculate_mean(example))



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file, "r") as csvfile:
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
    
    # Uses list comprehension again - quick way to build a new list in one line which is assigns to 'temp_float'
    # Convert all values to float for comparison
    temps_float = [float(value) for value in weather_data]

    # find min value using built-in min() function
    min_value = min(temps_float)

    # Find last index where min_value appears

# This loop starts from the end of the list and goes backwards toward the start.
# len(temps_float) - 1 is the index of the last element. -1 means “stop before index -1,” so it includes index 0.
# -1 as the step means “go backwards.”
# So it loops through indexes like [last, last-1, ..., 0].

    for i in range(len(temps_float) - 1, -1, -1):
        # So I'm comparing each element (from the end to the start) to the minimum value in the list.
        # This lets me find the last time that minimum appears.
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
    # Uses list comprehension again - quick way to build a new list in one line which is assigns to 'temp_float'
    # Convert all values to float for comparison as it loops through
    temps_float = [float(value) for value in weather_data]

    # find max value using built-in max() function
    max_value = max(temps_float)

    for num in range(len(temps_float) - 1, -1, -1):
        # So I'm comparing each element (from the end to the start) to the maximum value in the list.
        # This lets me find the last time that maximum appears.
        # At each step, we check whether the current element equals the maximum value we found earlier.
        # If it does, we immediately return it.
        if temps_float[num] == max_value:
            return max_value, num  


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
    # not really necessary, but keeping for consistency with other functions
    if not weather_data:
        return "No weather data available.\n"
    
    # counts how many sublists (days) are in the weather_data list
    # It will be used later in summary header
    num_days = len(weather_data)

    # Extract min and max temperatures directly (already in Celsius) using list comprehension (short loops that transform data)
    min_temps = [convert_f_to_c(day[1]) for day in weather_data]
    max_temps = [convert_f_to_c(day[2]) for day in weather_data]

    # Find lowest and highest temps and their last positions
    min_temp, min_index = find_min(min_temps)
    max_temp, max_index = find_max(max_temps)

    # Get corresponding dates for those temps
    min_date = convert_date(weather_data[min_index][0])
    # Make sure it is in a readable format
    max_date = convert_date(weather_data[max_index][0])

    # Calculate averages using my own helper function
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
        # Getting the date using the first element of the sublist (day[0]) and our convert_date function to make it readable.
        date = convert_date(day[0])
        min_c = format_temperature(convert_f_to_c(day[1]))
        max_c = format_temperature(convert_f_to_c(day[2]))

        daily_summary = (
            f"---- {date} ----\n"
            f"  Minimum Temperature: {min_c}\n"
            f"  Maximum Temperature: {max_c}\n"
        )

        summary_lines.append(daily_summary)
    # takes all the strings in the list and connects them with a newline between each.

    # change to f string 

    return f"{'\n'.join(summary_lines)}\n"

