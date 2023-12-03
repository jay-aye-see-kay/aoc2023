from dataclasses import dataclass


@dataclass
class Coord:
    x: int
    y: int


@dataclass
class BoundingBox:
    x_min: int
    x_max: int
    y_min: int
    y_max: int

    def contains(self, coord: Coord) -> bool:
        return (
            self.x_min <= coord.x <= self.x_max and self.y_min <= coord.y <= self.y_max
        )


@dataclass
class Number:
    value: str
    coord: Coord

    def bounding_box(self):
        x_min = self.coord.x - 1
        x_max = self.coord.x + len(self.value)
        y_min = self.coord.y - 1
        y_max = self.coord.y + 1
        return BoundingBox(x_min, x_max, y_min, y_max)


def parse_input(input: str):
    num_buffer = ""
    symbols: list[Coord] = []
    maybe_gears: list[Coord] = []
    numbers: list[Number] = []
    for y, line in enumerate(input.splitlines()):
        for x, char in enumerate(line):
            if char == ".":
                pass
            elif char.isdecimal():
                num_buffer += char
            else:
                symbols.append(Coord(x, y))

            if char == "*":
                maybe_gears.append(Coord(x, y))

            is_eol = x + 1 == len(line)
            if (is_eol or not char.isdecimal()) and num_buffer != "":
                # digit ended
                numbers.append(Number(num_buffer, Coord(x - len(num_buffer), y)))
                num_buffer = ""

    return (symbols, numbers, maybe_gears)


def part1(input: str):
    sum = 0
    symbols, numbers, _ = parse_input(input)
    for number in numbers:
        number_has_adjacent_symbol = False
        bounding_box = number.bounding_box()
        for symbol in symbols:
            if bounding_box.contains(symbol):
                number_has_adjacent_symbol = True
        if number_has_adjacent_symbol:
            sum += int(number.value)

    return sum


def part2(input: str):
    sum = 0
    _, numbers, maybe_gears = parse_input(input)
    for maybe_gear in maybe_gears:
        adj_numbers: list[Number] = []
        for number in numbers:
            if number.bounding_box().contains(maybe_gear):
                adj_numbers.append(number)
        if len(adj_numbers) == 2:
            sum += int(adj_numbers[0].value) * int(adj_numbers[1].value)

    return sum
