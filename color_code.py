MAJOR_COLORS = ['White', 'Red', 'Black', 'Yellow', 'Violet']
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

def color_pair_to_string(major_color, minor_color):
    return f'{major_color} {minor_color}'

def validate_pair_number(pair_number):
    max_pair_number = len(MAJOR_COLORS) * len(MINOR_COLORS)
    if not (1 <= pair_number <= max_pair_number):
        raise ValueError('Pair number out of range')

def get_color_from_pair_number(pair_number):
    validate_pair_number(pair_number)
    zero_based_pair_number = pair_number - 1
    major_index = zero_based_pair_number // len(MINOR_COLORS)
    minor_index = zero_based_pair_number % len(MINOR_COLORS)
    return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
    if major_color not in MAJOR_COLORS or minor_color not in MINOR_COLORS:
        raise ValueError('Color out of range')
    major_index = MAJOR_COLORS.index(major_color)
    minor_index = MINOR_COLORS.index(minor_color)
    return major_index * len(MINOR_COLORS) + minor_index + 1
