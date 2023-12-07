import unittest

from src.day07 import Hand, parse_input, part1

sample_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


class TestDay7(unittest.TestCase):
    def test_type_score(self):
        self.assertEqual(Hand("KKKKK").type_score(), 6)
        self.assertEqual(Hand("KKKKQ").type_score(), 5)
        self.assertEqual(Hand("KKKQQ").type_score(), 4)
        self.assertEqual(Hand("KKKQJ").type_score(), 3)
        self.assertEqual(Hand("KKQQJ").type_score(), 2)
        self.assertEqual(Hand("KKQJT").type_score(), 1)
        self.assertEqual(Hand("KQJT9").type_score(), 0)

    def test_less_than(self):
        self.assertEqual(Hand("KKKKQ").__lt__(Hand("KKKQQ")), False)
        self.assertEqual(Hand("KKKKQ").__lt__(Hand("KKKKK")), True)
        self.assertEqual(Hand("KKKKQ").__lt__(Hand("QKKKK")), False)

    def test_sort_hands(self):
        hands = parse_input(sample_input)
        hands.sort(key=lambda h: h[0])
        self.assertEqual("".join(hands[0][0].cards), "32T3K")
        self.assertEqual("".join(hands[1][0].cards), "KTJJT")
        self.assertEqual("".join(hands[2][0].cards), "KK677")
        self.assertEqual("".join(hands[3][0].cards), "T55J5")
        self.assertEqual("".join(hands[4][0].cards), "QQQJA")

    def test_part1_sample(self):
        self.assertEqual(part1(sample_input), 6440)

    def test_part1_real(self):
        with open("./inputs/day-07.txt") as f:
            self.assertEqual(part1(f.read()), 250602641)
