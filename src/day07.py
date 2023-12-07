from collections import Counter

card_points = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


class Hand:
    cards: list[str]

    def __init__(self, cards: str):
        self.cards = list(cards)

    def type_score(self):
        counts = Counter(self.cards).most_common(5)
        most_common = counts[0][1]
        if most_common == 5:
            return 6
        if most_common == 4:
            return 5
        if most_common == 3 and counts[1][1] == 2:
            return 4
        if most_common == 3 and counts[1][1] == 1:
            return 3
        if most_common == 2 and counts[1][1] == 2:
            return 2
        if most_common == 2 and counts[1][1] == 1:
            return 1
        if most_common == 1:
            return 0

    def __lt__(self, other):
        if self.type_score() != other.type_score():
            return self.type_score() < other.type_score()
        for c1, c2 in zip(self.cards, other.cards):
            if card_points[c1] != card_points[c2]:
                return card_points[c1] < card_points[c2]
        raise AssertionError("cards match exactly")


def parse_input(input: str) -> list[tuple[Hand, int]]:
    hands = []
    for line in input.splitlines():
        cards, score = line.split(" ")
        hands.append((Hand(cards), int(score)))
    return hands


def part1(input: str):
    sum = 0
    hands = parse_input(input)
    hands.sort(key=lambda h: h[0])
    for i, hand in enumerate(hands):
        sum += (i + 1) * hand[1]
    return sum
