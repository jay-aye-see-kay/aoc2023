import unittest

from src.day05 import Map, MapRange, parse_input, part1, part2

sample_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


class TestDay5(unittest.TestCase):
    def test_parse_input(self):
        seeds, maps = parse_input(sample_input)
        self.assertEqual(seeds, [79, 14, 55, 13])
        # self.assertEqual(
        #     maps["seed-to-soil"][0],
        #     MapRange(dest_start=50, source_start=98, length=2),
        # )
        # self.assertEqual(
        #     maps["humidity-to-location"][1],
        #     MapRange(dest_start=56, source_start=93, length=4),
        # )

    def test_map_lookup(self):
        map = Map([MapRange(50, 98, 2)])
        self.assertEqual(map.lookup(99), 51)

    def test_map_lookup_2(self):
        map = Map([MapRange(52, 50, 48)])
        self.assertEqual(map.lookup(53), 55)

    def test_part1_sample(self):
        location_num = part1(sample_input)
        self.assertEqual(location_num, 35)

    def test_part1_real(self):
        with open("./inputs/day-05.txt") as f:
            input = f.read()
        self.assertEqual(part1(input), 26273516)

    def test_part2_sample(self):
        location_num = part2(sample_input)
        self.assertEqual(location_num, 46)

    # def test_part2_real(self):
    #     with open("./inputs/day-05.txt") as f:
    #         input = f.read()
    #     self.assertEqual(part2(input), 0)
