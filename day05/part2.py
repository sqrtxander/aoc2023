from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    chunks = s.split('\n\n')

    init_seeds = [int(num) for num in chunks[0].split()[1:]]
    curr_stage = []
    for i in range(1, len(init_seeds), 2):
        curr_stage.append(
            (init_seeds[i - 1], init_seeds[i - 1] + init_seeds[i]))
    maps = []
    for chunk in chunks[1:]:
        lines = chunk.splitlines()[1:]
        maps.append([[int(num) for num in line.split()] for line in lines])
    for map_ in maps:
        new_stage = []
        sources = [line[0] for line in map_]
        for ran in curr_stage:
            done = ran[0]
            while done < ran[1]:
                new_ran = None
                for dest, source, length in map_:
                    if source <= done < source + length:
                        if ran[1] < source + length:
                            new_ran = (
                                done - source + dest,
                                ran[1] - source + dest
                            )
                        else:
                            new_ran = (
                                done - source + dest,
                                dest + length
                            )
                        break
                if new_ran is None:
                    higher_sources = [
                        source for source in sources
                        if source > done
                    ]
                    if higher_sources:
                        new_ran = (done, min(higher_sources))
                    else:
                        new_ran = (done, ran[1])
                new_stage.append(new_ran)
                done += new_ran[1] - new_ran[0]
        curr_stage = new_stage
    return (min(ran[0] for ran in curr_stage))


INPUT_S = '''\
seeds: 79 14 55 13

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
'''
EXPECTED = 46


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert solve(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(solve(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
