import json
import datetime

# temperature to color mapping
color_ranges = {
    "Ice Blue": range(-50, 30),
    "Dark Blue": range(30, 40),
    "Blue": range(40, 50),
    "Teal": range(50, 60),
    "Green": range(60, 70),
    "Yellow": range(70, 80),
    "Orange": range(80, 90),
    "Red": range(90, 200)
}

# color to yarn_color matching
yarn_map = {
    "Ice Blue": "Caron Soft Blue",
    "Dark Blue": "Caron Navy",
    "Blue": "Caron Sky",
    "Teal": "Sage",
    "Green": "",
    "Yellow": "",
    "Orange": "",
    "Red": "",
}

def main():
    """App Start"""
    # Check for JSON data:
    # If it exists, load data.
    # Else, create new JSON data
    try:
        #code that might fail
        with open("my_blanket_data.json") as f:
            data_list = json.load(f)
    
    except FileNotFoundError:
        data_list = []
        print("No data file found. Starting fresh.")
    # Print welcome message.
    print ("Welcome to the Crochet Temperature Blanket App")
    home_menu(data_list)

def home_menu(data_list):
    """Main navigation loop."""
    while True:
        print("\nHome Menu:")
        print("1. Select a date")
        print("2. View a saved day")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            date_selection(data_list)  # To be implemented
        elif choice == "2":
            if not data_list:
                print("No saved days yet.")
                continue
            date = input("Enter date (YYYY-MM-DD): ")
            view_summary(date, data_list)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def date_selection(data_list):
    """Handles date selection and workflow for a day.
    Placeholder for now.
    """
    # Ask user to pick a date, check for data, fetch temp, handle logic, etc.
    pass

def fetch_temperature():
    """Gets today's temperature."""
    # Try API to call for selected date's high temperature.
    # If API fails, ask user to enter manually (Fahrenheit).
    # Validate input (must be a number), return as integer.

def map_color(todays_temp):
    """Map temperature to color."""
    # Input: todays_temp (integer)
    # Loop through color_ranges to find which range matches
    # Return color string

def map_yarn_color(color):
    """Returns yarn color for given color."""
    # Input: color string
    # Lookup in yarn_map, return yarn color string

def record_day(date, data_list, temp, color, yarn_color, completed, pattern_viewed):
    """Save day's info."""
    # Create dictionary with all info.
    # Append it to master list (data_list).
    # Save updated list as JSON file.

def view_summary(date, data_list):
    """Show a summary for the selected day."""
    # Find date in data_list, print its info
    # If not found, inform user

# Placeholder for your master data list
data_list = []

if __name__ == "__main__":
    main()