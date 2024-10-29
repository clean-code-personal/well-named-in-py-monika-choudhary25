from color_constants import MAJOR_COLORS, MINOR_COLORS
from color_mapping import get_color_from_pair_number, get_pair_number_from_color
from test_color_mapping import test_pair_to_number,test_number_to_pair
from reference_manual import print_reference_manual

if __name__ == '__main__':
  test_number_to_pair(4, 'White', 'Brown')
  test_number_to_pair(5, 'White', 'Slate')
  test_pair_to_number('Black', 'Orange', 12)
  test_pair_to_number('Violet', 'Slate', 25)
  test_pair_to_number('Red', 'Orange', 7)

  print("Color Code Reference Manual:")
  print(print_reference_manual())
  print('Done :)')
