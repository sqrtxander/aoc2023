from __future__ import annotations

import argparse
import os.path

import pytest

import support

from itertools import combinations

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    galaxies = set()
    lines = s.splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.add((x, y))

    width = len(lines[0])
    height = len(line)

    y = 0
    while y < height:
        if all((x, y) not in galaxies for x in range(width)):
            galaxies = {
                (nx, ny + 1) if ny > y else (nx, ny)
                for nx, ny in galaxies
            }
            height += 1
            y += 1
        y += 1
    x = 0

    while x < width:
        if all((x, y) not in galaxies for y in range(height)):
            galaxies = {
                (nx + 1, ny) if nx > x else (nx, ny)
                for nx, ny in galaxies
            }
            width += 1
            x += 1
        x += 1
    total = 0

    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        total += abs(x1 - x2) + abs(y1 - y2)

    return total


INPUT_S = '''\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
'''
EXPECTED = 374


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
