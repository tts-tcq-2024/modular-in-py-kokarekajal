from test_color_code import test_number_to_pair, test_pair_to_number
from manual import generate_color_code_manual

if __name__ == '__main__':
    test_number_to_pair(4, 'White', 'Brown')
    test_number_to_pair(5, 'White', 'Slate')
    test_pair_to_number('Black', 'Orange', 12)
    test_pair_to_number('Violet', 'Slate', 25)
    print('All tests passed!')

    manual_text = generate_color_code_manual()
    print('\nColor Code Manual:')
    print(manual_text)
