from color_code import MAJOR_COLORS, MINOR_COLORS, get_pair_number_from_color, color_pair_to_string

def generate_color_code_manual():
    manual = []
    for major in MAJOR_COLORS:
        for minor in MINOR_COLORS:
            pair_number = get_pair_number_from_color(major, minor)
            manual.append(f'{pair_number}: {color_pair_to_string(major, minor)}')
    return '\n'.join(manual)

if __name__ == '__main__':
    manual_text = generate_color_code_manual()
    print(manual_text)
