color_to_temperature_ranges = {
    "Black": range(-30, 0),
    "Ice Blue": range(0, 30),
    "Dark Blue": range(30, 40), 
    "Blue": range(40, 50), 
    "Teal": range(50, 60), 
    "Green": range(60, 70),
    "Yellow": range(70, 80), 
    "Orange": range(80, 90), 
    "Red": range(90, 100),
    "Burgundy": range(100, 150)
}

def fetch_temperature(): #helper
    """Prompts user to manually enter the high temperature for the day."""
    # Later will use API to call for selected date's high temperature.
    
    while True: 
        temp_string = input("Enter today's high temperature. (in Fahrenheit)")
        try:
            todays_temp = int(temp_string)
            return todays_temp
        except ValueError:
            print("Please enter a valid number (ex. 57)")

def map_color(todays_temp): #helper
    """Map temperature to color."""
    for color, temp_range in color_to_temperature_ranges.items():
            if todays_temp in temp_range:
                return color
    return None

