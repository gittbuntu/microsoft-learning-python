loaded_config = """# Rocket Ship Configuration File!
fuel_tanks=4
oxygen_tanks=3
initial_propulsion_level=84
$ End of file"""

parsed_config = {}
for line in loaded_config.split('\n'):
    try:
        key, value = line.split('=')
        parsed_config[key] = value
    except ValueError:
        print(f'Unable to parse {line}')
print(parsed_config)


def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"