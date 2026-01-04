import datetime
import json

color_ranges = {
    "Black": range(-30, 0),
    "Ice Blue": range(0, 30),
    "Dark Blue": range(30, 40), 
    "Blue": range(40, 50), 
    "Teal": range(50, 60), 
    "Green": range(60, 70),
    "Yellow": range(70, 80), 
    "Orange": range(80, 90), 
    "Red": range(90, 100),
    "Burgundy": range(100, 150)
}

yarn_map = {
    "Black": "312 - Black",
    "Ice Blue": "381 - Light Blue", 
    "Dark Blue": "387 - Soft Navy", 
    "Blue": "385 - Royal", 
    "Teal": "631 - Light Sage", 
    "Green": "389 - Hunter Green",     
    "Yellow": "324 - Bright Yellow",
    "Orange": "254 - Pumpkin", 
    "Red": "319 - Cherry Red",
    "Burgundy": "378 - Claret"
}

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

def select_saved_date(data_list):
    """Prompt user to select a date that exists in saved entries."""
    
    if not data_list:
        print("No saved entries yet.")
        return None

    print("\nSaved Dates:")
    for entry in data_list:
        print(f"- {entry['date']}")

    while True:
        date_str = input("Enter the date you want to select (YYYY-MM-DD): ").strip()

        # Validate format
        try:
            dt = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Please enter as YYYY-MM-DD.")
            continue

        # Validate not future
        if dt > datetime.date.today():
            print("The date cannot be in the future. Try again.")
            continue

        # Validate it exists in saved entries
        if any(entry["date"] == date_str for entry in data_list):
            return date_str
        
        print("That date is not in your saved entries. Try again.")


def save_data(data_list):
    """Write the full data list to the JSON file safely."""
    try:
        with open("my_blanket_data.json", "w") as f:
            json.dump(data_list, f, indent=4)
        print("Data saved.")
    except Exception as e:
        print("Something went wrong. Data not saved.")
        print("Error:", e)

