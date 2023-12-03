import unittest

from src.day02 import Game, is_game_valid, part1, part2


class TestDay2(unittest.TestCase):
    def test_init_game(self):
        game = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(game.id, 5)
        self.assertEqual(game.sets[0], {"red": 6, "blue": 1, "green": 3})
        self.assertEqual(game.sets[1], {"red": 1, "blue": 2, "green": 2})

    def test_is_game_valid(self):
        game1 = Game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        game2 = Game(
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"
        )
        limits = {"red": 12, "green": 13, "blue": 14}
        self.assertEqual(is_game_valid(game1, limits), True)
        self.assertEqual(is_game_valid(game2, limits), False)

    def test_part1_real(self):
        with open("./inputs/day-02.txt") as f:
            input = f.read()
        self.assertEqual(part1(input), 2317)

    def test_part2_real(self):
        with open("./inputs/day-02.txt") as f:
            input = f.read()
        self.assertEqual(part2(input), 74804)
