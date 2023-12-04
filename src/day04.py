import re
from dataclasses import dataclass


@dataclass
class Card:
    id: int
    winning_nums: list[int]
    have_nums: list[int]

    def win_count(self):
        wins = set(self.winning_nums).intersection(set(self.have_nums))
        return len(wins)

    def points(self):
        win_count = self.win_count()
        if win_count == 0:
            return 0
        else:
            return 2 ** (self.win_count() - 1)


def parse_nums(nums: str) -> list[int]:
    cleaned = re.sub(" +", " ", nums.strip())
    return [int(n) for n in cleaned.split(" ") if n != ""]


def parse_input(input: str) -> list[Card]:
    cards: list[Card] = []
    for line in input.splitlines():
        s1, s2 = line.split(":")
        s3, s4 = s2.strip().split("|")
        id = int(re.sub(" +", " ", s1).split(" ")[1])
        winning_nums = parse_nums(s3)
        have_nums = parse_nums(s4)
        cards.append(Card(id, winning_nums, have_nums))
    return cards


def part1(input: str):
    cards = parse_input(input)
    total_points = 0
    for card in cards:
        total_points += card.points()
    return total_points
