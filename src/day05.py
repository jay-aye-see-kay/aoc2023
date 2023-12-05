from dataclasses import dataclass


@dataclass
class MapRange:
    dest_start: int
    source_start: int
    length: int


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
        maps[map_name] = map

    return seeds, maps


def map_lookup(map: Map, value: int):
    for m in map:
        if value >= m.source_start and value <= m.source_start + m.length:
            offset = value - m.source_start
            return m.dest_start + offset
    return value


def part1(input: str):
    seeds, maps = parse_input(input)
    locations = []
    for seed in seeds:
        num = seed
        for _, map in maps.items():
            num = map_lookup(map, num)
        locations.append(num)
    return min(locations)
