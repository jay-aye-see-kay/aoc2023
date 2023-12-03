import unittest

from src.day03 import parse_input, part1, part2

sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


class TestDay2(unittest.TestCase):
    def test_parse_input(self):
        symbols, numbers = parse_input(sample_input)
        self.assertEqual(len(symbols), 6)
        self.assertEqual(len(numbers), 10)

    def test_day1_sample(self):
        self.assertEqual(part1(sample_input), 4361)

    def test_part1_real(self):
        with open("./inputs/day-03.txt") as f:
            input = f.read()
        self.assertEqual(part1(input), 530849)


# def test_part2_real(self):
#     with open("./inputs/day-02.txt") as f:
#         input = f.read()
#     self.assertEqual(part2(input), 74804)
