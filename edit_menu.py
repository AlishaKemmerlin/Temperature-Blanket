from helpers import (fetch_temperature, map_color, map_yarn_color, select_saved_date)

def edit_menu(data_list):
    while True:
        print("\nEdit Menu:")
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

def delete_one_entry(data_list):
    date = select_saved_date(data_list)
    for record in data_list:
        if record["date"] == date:
            yes_no = input(f"Are you sure you want to delete the entry for {date}? (y/n): ").lower()
            if yes_no == "y":
                data_list.remove(record)
                print(f"Entry for {date} deleted.")
                return
            else:
                print("Deletion cancelled.")
                return
    print("No entry found for that date.")

def delete_all_entries(data_list):
    yes_no = input("Are you sure you want to delete ALL entries? (y/n): ").lower()
    if yes_no == "y":
        confirm = input("This will delete all your saved entries. This option cannot be changed. Are you certain you are sure? (y/n): ").lower()
        if confirm == "y":
            data_list.clear()
            print("All entries deleted. Starting fresh!")
    else:
        print("Deletion cancelled.")

def edit_temperature(data_list):
    date = select_saved_date(data_list)
    for record in data_list:
        if record["date"] == date:
            print(f"Current temperature: {record['temperature']}°F") 
            print(f"Current color: {record['color']}")
            new_temp = fetch_temperature()
            new_color = map_color(new_temp)
            new_yarn_color = map_yarn_color(new_color)
            yes_no = input(f"The new temperature is {new_temp}°F with color {new_color} and yarn color {new_yarn_color}. Confirm update? (y/n): ").lower()
            if yes_no != "y":
                print("Update cancelled.")
                return
            record["temperature"] = new_temp
            record["color"] = new_color
            record["yarn_color"] = new_yarn_color
            print(f"Entry for {date} updated.")
            return
    print("No entry found for that date.")
