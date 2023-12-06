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
    lowest = binarySearch(range(0, time // 2), min_dist, time)
    highest = binarySearchRev(range(time // 2, time - 1), min_dist, time)
    return highest - lowest


def binarySearchRev(range_: range, min_dist: int, total_time: int) -> int:
    first = range_.start
    last = range_.stop
    found = False

    while first <= last and not found:
        pos = 0
        hold_time = (first + last) // 2
        dist = hold_time * (total_time - hold_time)
        if dist == min_dist:
            pos = hold_time
            found = True
        else:
            if min_dist > dist:
                last = hold_time - 1
            else:
                first = hold_time + 1
    return pos or hold_time


def binarySearch(range_: range, min_dist: int, total_time: int) -> int:
    first = range_.start
    last = range_.stop
    found = False

    while first <= last and not found:
        pos = 0
        hold_time = (first + last) // 2
        dist = hold_time * (total_time - hold_time)
        if dist == min_dist:
            pos = hold_time
            found = True
        else:
            if min_dist < dist:
                last = hold_time - 1
            else:
                first = hold_time + 1
    return pos or hold_time
