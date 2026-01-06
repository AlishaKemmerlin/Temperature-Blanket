from helpers.edit_entry import delete_one_entry, delete_all_entries, edit_temperature
from helpers.display import divider_line

def edit_menu(data_list):
    while True:
        divider_line()
        print("\nEdit Menu:")
        divider_line()
        print("1. Delete one entry")
        print("2. Delete ALL entries")
        print("3. Change the temperature on a day")
        print("4. Return to Home Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            delete_one_entry(data_list)
        elif choice == "2":
            delete_all_entries(data_list)
        elif choice == "3":
            edit_temperature(data_list)
        elif choice == "4":
            print("Returning to Home Menu.")
            return
        else:
            print("Invalid choice. Try again.")


