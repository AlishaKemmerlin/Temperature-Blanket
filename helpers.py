import datetime
import json

#temperature helpers
def fetch_temperature(): #helper
    """Prompts user to manually enter the high temperature for the day."""
    # Later will use API to call for selected date's high temperature.
    
    while True: 
        temp_string = input("Enter today's high temperature. (in Fahrenheit)")
        try:
            todays_temp = int(temp_string)
            return todays_temp
        except ValueError:
            print("Please enter a valid number (ex. 57)")

def map_color(todays_temp): #helper
    """Map temperature to color."""
    for color, temp_range in color_ranges.items():
            if todays_temp in temp_range:
                return color
            
def map_yarn_color(temp_color):
    return yarn_map.get(temp_color)


#date helpers
def date_selection(): #helper
    """Get today's date, either from system or user input."""
    try:
        # Try to get today's date from the system
        todays_date = datetime.date.today()
        return str(todays_date)
    except Exception: 
        # If system date fails, ask the user (until input is valid and not future)
        while True:
            todays_date = input("Input the date (YYYY-MM-DD): ")
            try:
                dt = datetime.datetime.strptime(todays_date, "%Y-%m-%d").date()
                if dt > datetime.date.today():
                    print("The date cannot be in the future. Please try again.")
                else:
                    return todays_date  # Always returning 'todays_date'
            except ValueError:
                print("Invalid date format. Please enter as YYYY-MM-DD.")

def select_saved_date(): #helper
    """Prompt user to select a date to view."""
    while True:
        date_str = input("Enter the date you want to view (YYYY-MM-DD): ")
        try:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            if dt > datetime.date.today():
                print("The date cannot be in the future. Try again.")
            else:
                return date_str
        except ValueError:
            print("Invalid date format. Please enter as YYYY-MM-DD.")

def save_data(data_list):
    """Write the full data list to the JSON file safely."""
    try:
        with open("my_blanket_data.json", "w") as f:
            json.dump(data_list, f, indent=4)
        print("Data saved.")
    except Exception as e:
        print("Something went wrong. Data not saved.")
        print("Error:", e)

