def parse_line(line: str):
    items = filter(lambda n: n != "" and ":" not in n, line.split(" "))
    return list(map(lambda n: int(n), items))


def parse_input(input: str):
    times, distances = input.splitlines()
    return list(zip(parse_line(times), parse_line(distances)))


def parse_input_2(input: str):
    times, distances = input.splitlines()
    return [
        int(times.replace("Time:", "").replace(" ", "")),
        int(distances.replace("Distance:", "").replace(" ", "")),
    ]


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
    time, min_dist = parse_input_2(input)
    winning_races = []
    for hold_time in range(1, time):
        dist = hold_time * (time - hold_time)
        if dist > min_dist:
            winning_races.append(dist)
    return len(winning_races)
