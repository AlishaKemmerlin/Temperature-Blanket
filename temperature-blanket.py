import json
import datetime

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

yarn_map = {
    "Ice Blue": "Light Blue", 
    "Dark Blue": "Soft Navy", 
    "Blue": "Cobalt Blue", 
    "Teal": "Pale Teal", 
    "Green": "Castleton Green",     
    "Yellow": "Caron Baby Sunshine",
    "Orange": "Pumpkin", 
    "Red": "Cherry Red"
}

def main():
    """App Start"""
    try:
        with open("my_blanket_data.json") as f:
            data_list = json.load(f)
    except FileNotFoundError:
        data_list = []
        print("No data file found. Starting fresh.")
    # Print welcome message.
    print ("Welcome to the Crochet Weather Blanket App")
    print (
        """This app will give you a suggested yarn color 
        to start your own weather blanket.
        Each yarn color suggest is from Red Heart Super Saver. 
        But you can of course choose your own color.""")   
    home_menu(data_list)

def home_menu(data_list):
    """Main navigation loop."""
    while True:
        print("\nHome Menu:")
        print("1. Select a date")
        print("2. View a saved day")
        print("3. View Granny Square Pattern")
        print("4. Exit")

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
            print("Granny Square Pattern:")
            print(
                """[Pattern details would go here]"""
            )
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



def fetch_temperature():
    """Prompts user to manually enter today's high temperature. 
    Later will use API to call for selected date's high temp. """
    while True: 
        temp_string = input("Enter today's high temperature. (in Fahrenheit)")
        try:
            todays_temp = int(temp_string)
            return todays_temp
        except ValueError:
            print("Please enter a valid number (ex. 57)")


def map_color(todays_temp):
    """Map temperature to color."""
    for color, temp_range in color_ranges.items():
            if todays_temp in temp_range:
                return temp_color

temp_color = map_color(todays_temp)

if temp_color is None:
    yes_no = input("No yarn color found. Would you like to try again? (y/n)").lower()
    if yes_no.lower() == "y":
        fetch_temperature()
    else:
        temp_color = input("Enter a color: red, orange, yellow, green, teal, blue, dark blue, ice blue").lower()
def date_selection(data_list):
    """Handles date selection and workflow for a day.
    Placeholder for now.
    """
    todays_date = input("Input the date: YYYY-MM-DD")
    for record in data_list:
        if record["date"] == todays_date:
            print("Record exists")
            view_summary(todays_date, data_list)
            return


def map_yarn_color(temp_color):
    return yarn_map.get(temp_color)


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