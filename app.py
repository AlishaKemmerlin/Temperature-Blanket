import json

from helpers.create_entry import create_entry
from helpers.dates import date_selection, select_saved_date
from helpers.storage import load_data
from edit_menu import edit_menu
from helpers.view_entry import view_summary
from helpers.display import welcome_header, main_menu_header, divider_line, exit_message
from helpers.instructions import blanket_instructions, granny_square_pattern, pause

def main():
    """App Start"""
    data_list = load_data()

    welcome_header()
    blanket_instructions()
    home_menu(data_list)

def home_menu(data_list):
    """Main navigation loop."""
    while True:
        main_menu_header()
        print("1. Today's Temperature")
        print("2. View a saved day")
        print("3. Edit Menu")
        print("4. Instructions Menu")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            todays_date = date_selection()
            create_entry(todays_date, data_list)  # To be implemented
        elif choice == "2":
            if not data_list:
                print("No saved days yet.")
                continue
            date = select_saved_date(data_list)
            view_summary(date, data_list)
        elif choice == "3":
            edit_menu(data_list)
        elif choice == "4":
            instructions_menu()
        elif choice == "5":
            exit_message()
            break
        else:
            print("Invalid choice. Please try again.")

def instructions_menu():
    """Display instructions menu."""
    divider_line()
    print("Instructions Menu:")
    divider_line()
    print("1. Blanket Instructions")
    print("2. Granny Square Pattern")
    print("3. Return to Home Menu")

    choice = input("Choose an option: ")

    if choice == "1":
        blanket_instructions()
        pause()
    elif choice == "2":
        granny_square_pattern()
        pause()
    elif choice == "3":
        return
    else:
        print("Invalid choice. Try again.")

# This runs the app only when this file is executed directly.
# It prevents the program from auto‑running if the file is imported elsewhere.
if __name__ == "__main__":
    main()
