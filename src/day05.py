class MapRange:
    def __init__(self, dest_start: int, source_start: int, length: int):
        self.source_start = source_start
        self.source_end = source_start + length
        self.offset = dest_start - source_start
        self.length = length


class Map:
    def __init__(self, ranges: list[MapRange]):
        self.ranges = ranges

    def lookup(self, value: int):
        for m in self.ranges:
            if value >= m.source_start and value <= m.source_end:
                return value + m.offset
        return value


def parse_input(input: str):
    maps: dict[str, Map] = {}

    paragraphs = input.split("\n\n")
    seeds_str = paragraphs[0].replace("seeds: ", "").strip()
    seeds = [int(s) for s in seeds_str.split(" ")]

    for para in paragraphs[1:]:
        lines = para.splitlines()
        map_name = lines[0].replace(" map:", "")
        map_ranges = []
        for values_str in lines[1:]:
            map_values = [int(s) for s in values_str.split(" ")]
            map_ranges.append(MapRange(*map_values))
        maps[map_name] = Map(map_ranges)

    return seeds, maps


def seed_to_location(maps: dict[str, Map], seed: int):
    num = seed
    for _, map in maps.items():
        num = map.lookup(num)
    return num


def part1(input: str):
    seeds, maps = parse_input(input)
    locations = []
    for seed in seeds:
        locations.append(seed_to_location(maps, seed))
    return min(locations)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def part2(input: str):
    seeds, maps = parse_input(input)
    min_location = 100000000000000000
    for i, (seeds_start, seeds_len) in enumerate(chunks(seeds, 2)):
        for seed in range(seeds_start, seeds_start + seeds_len):
            if seed % 100000 == 0:
                print(f"{100*((seed-seeds_start)/seeds_len):.2f}% through range {i+1}")
            location = seed_to_location(maps, seed)
            if location < min_location:
                min_location = location
    return min_location


if __name__ == "__main__":
    with open("./inputs/day-05-mini.txt") as f:
        input = f.read()
    print(part2(input))
