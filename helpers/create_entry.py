from helpers.temperature import fetch_temperature, map_color
from helpers.colors import map_yarn_color
from helpers.view_entry import view_summary
from helpers.storage import save_data


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
            temp_color = input("Enter a color \n(burgundy, red, orange, yellow, green, teal, blue, dark blue, ice blue, black):").strip().title()
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
    save_data(data_list)
    return data_list