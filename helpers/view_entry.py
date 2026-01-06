from helpers.instructions import pause
from helpers.create_entry import create_entry

def view_summary(date, data_list):
    # Look for the date
    for record in data_list:
        if record["date"] == date:
            print("\n--- Day Summary ---")
            print(f"Date: {record['date']}")
            print(f"Temperature: {record['temperature']}°F")
            print(f"Color: {record['color']}")
            print(f"Yarn Color: {record['yarn_color']}")
            pause()
            return

    # If we reach here, the date wasn't found
    print("No entry found for that date.")
    choice = input("Would you like to create an entry for this date? (y/n): ").strip().lower()

    if choice == "y":
        create_entry(date)   # <-- use the date the user typed
    else:
        print("Returning to Home Menu.")        