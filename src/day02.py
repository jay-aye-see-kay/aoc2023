GameSet = dict[str, int]


class Game:
    id: int
    sets: list[GameSet]

    def __init__(self, input_line: str):
        s1, s2 = input_line.split(":", 1)
        self.id = int(s1.strip().split()[1])
        self.sets = []

        game_sets = s2.split(";")
        for game_set in game_sets:
            self.sets.append({})
            colors = game_set.split(",")
            for color in colors:
                color = color.strip()
                count, color_name = color.split()
                self.sets[-1][color_name] = int(count)


def is_set_valid(game_set: GameSet, limits: GameSet):
    for color, count in game_set.items():
        color_limit = limits.get(color)
        if color_limit is not None and count > color_limit:
            return False
    return True


def is_game_valid(game: Game, limits: GameSet):
    for game_set in game.sets:
        if not is_set_valid(game_set, limits):
            return False
    return True


def part1(input: str):
    limits = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for line in input.splitlines():
        game = Game(line)
        if is_game_valid(game, limits):
            sum += game.id
    return sum


def part2(input: str):
    return 0
