import unittest

from src.day08 import parse_input, part1

sample_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""


class TestDay8(unittest.TestCase):
    def test_parse_input(self):
        instructions, network = parse_input(sample_input)
        self.assertEqual(instructions, ["L", "L", "R"])
        self.assertEqual(
            network,
            {
                "AAA": ("BBB", "BBB"),
                "BBB": ("AAA", "ZZZ"),
                "ZZZ": ("ZZZ", "ZZZ"),
            },
        )

    def test_part1_sample(self):
        self.assertEqual(part1(sample_input), 6)

    def test_part1_real(self):
        with open("./inputs/day-08.txt") as f:
            self.assertEqual(part1(f.read()), 19099)
