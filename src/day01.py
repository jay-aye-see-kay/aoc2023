def get_first_and_last_digit(input_line: str):
    digits = list(filter(str.isdigit, input_line))
    return int(digits[0] + digits[-1])


def part1(input: str):
    sum = 0
    for line in input.splitlines():
        sum += get_first_and_last_digit(line)
    return sum


numbers: list[tuple[str, str]] = [
    ("one", "1"),
    ("two", "2"),
    ("three", "3"),
    ("four", "4"),
    ("five", "5"),
    ("six", "6"),
    ("seven", "7"),
    ("eight", "8"),
    ("nine", "9"),
]


def get_first_and_last_digit_2(input_line: str):
    digits = []
    for i, char in enumerate(input_line):
        for long_num, short_num in numbers:
            char_is_number = char == short_num or input_line[i:].startswith(long_num)
            if char_is_number:
                digits.append(short_num)
    return int(digits[0] + digits[-1])


def part2(input: str):
    sum = 0
    for line in input.splitlines():
        sum += get_first_and_last_digit_2(line)
    return sum
