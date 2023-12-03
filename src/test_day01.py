import unittest

from src.day01 import get_first_and_last_digit, part1


class TestReplaceNames(unittest.TestCase):
    def test_get_first_and_last_digit(self):
        sample_lines = [
            ["1abc2", 12],
            ["pqr3stu8vwx", 38],
            ["a1b2c3d4e5f", 15],
            ["treb7uchet", 77],
        ]
        for sample in sample_lines:
            self.assertEqual(get_first_and_last_digit(sample[0]), sample[1])

    def test_part1_sample(self):
        input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
        self.assertEqual(part1(input), 142)

    def test_part1_real(self):
        with open("./inputs/day-01.txt") as f:
            input = f.read()
        self.assertEqual(part1(input), 56397)
