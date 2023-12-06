def parse_line(line: str):
    items = filter(lambda n: n != "" and ":" not in n, line.split(" "))
    return list(map(lambda n: int(n), items))


def parse_input(input: str):
    times, distances = input.splitlines()
    return list(zip(parse_line(times), parse_line(distances)))


def part1(input: str):
    sum = 1
    races = parse_input(input)
    for time, min_dist in races:
        winning_races = []
        for hold_time in range(1, time):
            dist = hold_time * (time - hold_time)
            if dist > min_dist:
                winning_races.append(dist)
        sum *= len(winning_races)
    return sum


def part2(input: str):
    return 0
