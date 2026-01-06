yarn_map = {
    "Black": "312 - Black",
    "Ice Blue": "381 - Light Blue", 
    "Dark Blue": "387 - Soft Navy", 
    "Blue": "385 - Royal", 
    "Teal": "631 - Light Sage", 
    "Green": "389 - Hunter Green",     
    "Yellow": "324 - Bright Yellow",
    "Orange": "254 - Pumpkin", 
    "Red": "319 - Cherry Red",
    "Burgundy": "378 - Claret"
}


def map_yarn_color(temp_color):
    """Map temperature color to yarn color."""
    return yarn_map.get(temp_color)

