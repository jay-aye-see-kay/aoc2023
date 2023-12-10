import unittest

from src.day08 import parse_input, part1, part2

sample_input = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

sample_input2 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
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

    def test_part2_sample(self):
        self.assertEqual(part2(sample_input2), 6)

    def test_part2_real(self):
        with open("./inputs/day-08.txt") as f:
            self.assertEqual(part2(f.read()), 17099847107071)
