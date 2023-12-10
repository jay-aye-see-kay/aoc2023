import re
from math import lcm

Instructions = list[str]

Network = dict[str, tuple[str, str]]


def parse_input(input: str):
    instructions_str, network_str = input.split("\n\n")
    instructions: Instructions = list(instructions_str)
    network: Network = {}
    for line in network_str.splitlines():
        match = re.search("(?P<key>.*) = \((?P<left>.*), (?P<right>.*)\)", line)
        if match:
            key, left, right = match.groups()
            network[key] = (left, right)
    return instructions, network


def travel_until(start: str, end_cond, instructions: Instructions, network: Network):
    step = 0
    cur = start
    while not end_cond(cur):
        ins = instructions[step % len(instructions)]
        cur = network[cur][0 if ins == "L" else 1]
        step += 1
    return step


def part1(input: str):
    instructions, network = parse_input(input)
    return travel_until("AAA", lambda n: n == "ZZZ", instructions, network)


def part2(input: str):
    instructions, network = parse_input(input)
    starting_points = [n for n in network.keys() if n.endswith("A")]
    counts_until_repeat = []
    for start in starting_points:
        c = travel_until(start, lambda n: n.endswith("Z"), instructions, network)
        counts_until_repeat.append(c)
    return lcm(*counts_until_repeat)
