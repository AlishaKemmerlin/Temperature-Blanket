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