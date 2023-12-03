def get_first_and_last_digit(input_line: str):
    digits = list(filter(str.isdigit, input_line))
    return int(digits[0] + digits[-1])


def part1(input: str):
    sum = 0
    for line in input.splitlines():
        sum += get_first_and_last_digit(line)
    return sum
