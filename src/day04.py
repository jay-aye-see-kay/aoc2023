import re
from dataclasses import dataclass


@dataclass
class Card:
    id: int
    winning_nums: list[int]
    have_nums: list[int]
    copies_won: int

    def win_count(self):
        wins = set(self.winning_nums).intersection(set(self.have_nums))
        return len(wins)

    def points(self):
        win_count = self.win_count()
        if win_count == 0:
            return 0
        else:
            return 2 ** (self.win_count() - 1)


def clean_spaces(input: str):
    return re.sub(" +", " ", input.strip())


def parse_nums(nums: str) -> list[int]:
    return [int(n) for n in clean_spaces(nums).split(" ")]


def parse_input(input: str) -> list[Card]:
    cards: list[Card] = []
    for line in input.splitlines():
        s1, s2 = line.split(":")
        s3, s4 = clean_spaces(s2).split("|")
        cards.append(
            Card(
                id=int(clean_spaces(s1).split(" ")[1]),
                winning_nums=parse_nums(s3),
                have_nums=parse_nums(s4),
                copies_won=1,
            )
        )
    return cards


def part1(input: str):
    cards = parse_input(input)
    total_points = 0
    for card in cards:
        total_points += card.points()
    return total_points


def part2(input: str):
    total_points = 0
    cards = parse_input(input)
    for i, card in enumerate(cards):
        total_points += card.copies_won
        for point in range(card.win_count()):
            cards[i + point + 1].copies_won += card.copies_won
    return total_points
