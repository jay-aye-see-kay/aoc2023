import unittest

from src.day04 import parse_input, part1, part2

sample_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


class TestDay4(unittest.TestCase):
    def test_parse_input(self):
        cards = parse_input(sample_input)
        self.assertEqual(len(cards), 6)

    def test_part1_sample(self):
        count = part1(sample_input)
        self.assertEqual(count, 13)

    def test_part1_real(self):
        with open("./inputs/day-04.txt") as f:
            input = f.read()
        self.assertEqual(part1(input), 22674)

    def test_part2_sample(self):
        count = part2(sample_input)
        self.assertEqual(count, 30)

    def test_part2_real(self):
        with open("./inputs/day-04.txt") as f:
            input = f.read()
        self.assertEqual(part2(input), 5747443)
