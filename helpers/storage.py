import json

def save_data(data_list):
    """Write the full data list to the JSON file safely."""
    try:
        with open("my_blanket_data.json", "w") as f:
            json.dump(data_list, f, indent=4)
        print("Data saved.")
    except Exception as e:
        print("Something went wrong. Data not saved.")
        print("Error:", e)

def load_data():
    """Load data from the JSON file safely."""
    try:
        with open("my_blanket_data.json", "r") as f:
            data_list = json.load(f)
        return data_list
    except FileNotFoundError:
        print("No data file found. Starting fresh.")
        return []
    except json.JSONDecodeError:
        print("Data file is corrupted. Starting fresh.")
        return []
    except Exception as e:
        print("An unexpected error occurred while loading data. Starting fresh.")
        print("Error:", e)
        return []