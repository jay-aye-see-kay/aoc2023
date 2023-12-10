import re

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


def part1(input: str):
    instructions, network = parse_input(input)
    step = 0
    cur = "AAA"
    while cur != "ZZZ":
        ins = instructions[step % len(instructions)]
        cur = network[cur][0 if ins == "L" else 1]
        step += 1
    return step
