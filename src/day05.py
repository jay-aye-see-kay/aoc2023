class MapRange:
    def __init__(self, dest_start: int, source_start: int, length: int):
        self.source_start = source_start
        self.source_end = source_start + length
        self.offset = dest_start - source_start
        self.length = length


Map = list[MapRange]


def parse_input(input: str):
    maps: dict[str, Map] = {}

    paragraphs = input.split("\n\n")
    seeds_str = paragraphs[0].replace("seeds: ", "").strip()
    seeds = [int(s) for s in seeds_str.split(" ")]

    for para in paragraphs[1:]:
        lines = para.splitlines()
        map_name = lines[0].replace(" map:", "")
        map = []
        for values_str in lines[1:]:
            map_values = [int(s) for s in values_str.split(" ")]
            map.append(MapRange(*map_values))
        sorted(map, key=lambda m: m.length)
        maps[map_name] = map

    return seeds, maps


def map_lookup(map: Map, value: int):
    for m in map:
        if value >= m.source_start and value <= m.source_end:
            return value + m.offset
    return value


def seed_to_location(maps: dict[str, Map], seed: int):
    num = seed
    for _, map in maps.items():
        num = map_lookup(map, num)
    return num


def part1(input: str):
    seeds, maps = parse_input(input)
    locations = []
    for seed in seeds:
        locations.append(seed_to_location(maps, seed))
    return min(locations)


def part2(input: str):
    seeds, maps = parse_input(input)
    min_location = 100000000000000000
    x = 0
    while x < len(seeds):
        seeds_start = seeds[x]
        seeds_len = seeds[x + 1]
        x += 2
        for seed in range(seeds_start, seeds_start + seeds_len):
            if seed % 10000 == 0:
                print(f"{100*((seed-seeds_start)/seeds_len)}% through range {(x/2)-1}")
            location = seed_to_location(maps, seed)
            if location < min_location:
                min_location = location
    return min_location


if __name__ == "__main__":
    with open("./inputs/day-05-mini.txt") as f:
        input = f.read()
    print(part2(input))
