import json
import datetime
from edit_menu import (
    edit_menu,
    delete_one_entry,
    delete_all_entries,
    edit_temperature,
    select_saved_date
)


color_ranges = {
    "Ice Blue": range(-50, 30), "Dark Blue": range(30, 40),
    "Blue": range(40, 50), "Teal": range(50, 60), "Green": range(60, 70),
    "Yellow": range(70, 80), "Orange": range(80, 90), "Red": range(90, 200)
}

yarn_map = {
    "Ice Blue": "Light Blue", "Dark Blue": "Soft Navy", 
    "Blue": "Cobalt Blue", "Teal": "Pale Teal", "Green": "Castleton Green",     "Yellow": "Caron Baby Sunshine",
    "Orange": "Pumpkin", "Red": "Cherry Red"
}

def main():
    """App Start"""
    try:
        with open("my_blanket_data.json") as f:
            data_list = json.load(f)
    except FileNotFoundError:
        data_list = []
        print("No data file found. Starting fresh.")
    except json.JSONDecodeError:
        data_list = []
        print("Data file is corrupted. Starting fresh.")
    except Exception as e:
        data_list = []
        print("An unexpected error occurred while loading data. Starting fresh.")

    print ("Welcome to the Crochet Weather Blanket App\n")
    blanket_instructions()
    home_menu(data_list)

def home_menu(data_list):
    """Main navigation loop."""
    while True:
        print("\nHome Menu:")
        print("1. Today's Temperature")
        print("2. View a saved day")
        print("3. View Granny Square Pattern")
        print("4. Blanket Instructions")
        print("5. Edit Menu")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            todays_date = date_selection()
            create_entry(todays_date, data_list)  # To be implemented
        elif choice == "2":
            if not data_list:
                print("No saved days yet.")
                continue
            date = select_saved_date()
            view_summary(date, data_list)
        elif choice == "3":
            granny_square_pattern()
        elif choice == "4":
            blanket_instructions()
        elif choice == "5":
            edit_menu(data_list)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


def fetch_temperature():
    """Prompts user to manually enter the high temperature for the day."""
    # Later will use API to call for selected date's high temperature.
    
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
                return color
 
def date_selection():
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

def select_saved_date():
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

def map_yarn_color(temp_color):
    return yarn_map.get(temp_color)

def create_entry(todays_date, data_list):
    for record in data_list:
        if record["date"] == todays_date:
            print("Record exists")
            view_summary(todays_date, data_list)
            return
    todays_temp = fetch_temperature()
    temp_color = map_color(todays_temp)
    if temp_color is None:
        yes_no = input("No temperature color found. Would you like to try again? (y/n)").lower()
        if yes_no.lower() == "y":
            todays_temp = fetch_temperature()
            temp_color = map_color(todays_temp)
        else:
            temp_color = input("Enter a color: red, orange, yellow, green, teal, blue, dark blue, ice blue").strip().title()
    yarn_color = map_yarn_color(temp_color)
    print(f"The temperature in your area is: {todays_temp}°F. \nToday's yarn color is: {yarn_color}")
    record_day(todays_date, data_list, todays_temp, temp_color, yarn_color, completed=True)


def record_day(todays_date, data_list, todays_temp, temp_color, yarn_color, completed):
    # create a dictionary entry for the day

    day_entry = {
    "date": todays_date,
    "temperature": todays_temp,
    "color": temp_color,
    "yarn_color": yarn_color,
    "completed": completed
    }
    data_list.append(day_entry)
    try:
        with open("my_blanket_data.json", "w") as f:
            json.dump(data_list, f)
            print("Data Saved")
    except Exception as e:
        print("Something went wrong. Data not saved. Error:", e)

def view_summary(date, data_list):
    for record in data_list:
        if record["date"] == date:
            print("\n--- Day Summary ---")
            print(f"Date: {record['date']}")
            print(f"Temperature: {record['temperature']}°F")
            print(f"Color: {record['color']}")
            print(f"Yarn Color: {record['yarn_color']}")
            return
    print("No entry found for that date.")

def granny_square_pattern():
    """Display granny square pattern instructions."""
    print(
        "Simple Granny Square Pattern (Magic Ring Version)\n"
        "\n"
        "Round 1:\n"
        "- Make a magic ring. (or chain 4, join with slip stitch to form a ring)\n"
        "- Ch 3 (counts as dc), then work 2 dc into the ring.\n"
        "- *Ch 2, 3 dc into the ring* — repeat 3 more times.\n"
        "- Ch 2 and pull the ring closed.\n"
        "- Join with a sl st to the top of the beginning ch-3.\n"
        "\n"
        "Round 2:\n"
        "- Sl st into the next ch-2 corner space.\n"
        "- Ch 3, 2 dc, ch 2, 3 dc in the same corner.\n"
        "- In each remaining corner: 3 dc, ch 2, 3 dc.\n"
        "- Join with a sl st.\n"
        "\n"
        "Round 3 and Beyond:\n"
        "- In each corner: 3 dc, ch 2, 3 dc.\n"
        "- In each side space: 3 dc.\n"
        "- Join with a sl st at the end of each round.\n"
        "\n"
        "Continue until your square is the size you want!"
    )

def blanket_instructions():
    print(
        """Temperature Blanket Instructions (12‑Square Version)
        This project uses one large granny square for each month of the year.

        How it works:
        - You will make 12 squares total — one for each month.
        - Each day of the month adds ONE round to that month's square.
        - Day 1 has TWO rounds:
            • the center round (Round 1)
            • the temperature round for Day 1
        - By the end of the month, your square will have 29–32 rounds"
          depending on how many days are in that month"
        - Each round's color is based on that day's high temperature.
        As you finish each month, you can join the squares right away"
        or wait until the end of the year.  Either way works!"
        
        When the year is complete, you'll have 12 beautiful squares that
        show the temperature story of your entire year."""
    )

# This runs the app only when this file is executed directly.
# It prevents the program from auto‑running if the file is imported elsewhere.
if __name__ == "__main__":
    main()