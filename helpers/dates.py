import datetime

def date_selection(): #helper
    """Get today's date, either from system or user input."""
    try:
        # Preferably try to get system date
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
