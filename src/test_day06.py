import unittest

from src.day06 import parse_input, parse_input_2, part1, part2

sample_input = """Time:      7  15   30
Distance:  9  40  200
"""


class TestDay6(unittest.TestCase):
    def test_parse_input(self):
        runs = parse_input(sample_input)
        self.assertEqual(runs, [(7, 9), (15, 40), (30, 200)])

    def test_part1_sample(self):
        self.assertEqual(part1(sample_input), 288)

    def test_part1_real(self):
        with open("./inputs/day-06.txt") as f:
            input = f.read()
        self.assertEqual(part1(input), 1710720)

    def test_parse_input_2(self):
        runs = parse_input_2(sample_input)
        self.assertEqual(runs, [71530, 940200])

    def test_part2_sample(self):
        self.assertEqual(part2(sample_input), 71503)

    def test_part2_real(self):
        with open("./inputs/day-06.txt") as f:
            input = f.read()
        self.assertEqual(part2(input), 35349468)
