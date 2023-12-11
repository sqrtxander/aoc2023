from __future__ import annotations

import argparse
import os.path

import pytest

import support

from itertools import combinations

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str, gap: int) -> int:
    galaxies = set()

    lines = s.splitlines()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.add((x, y))

    width = len(lines[0])
    height = len(line)

    y_gaps = {
        y for y in range(height)
        if all((x, y) not in galaxies for x in range(width))
    }

    x_gaps = {
        x for x in range(width)
        if all((x, y) not in galaxies for y in range(height))
    }

    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        x_dist = abs(x2 - x1) + (gap - 1) * \
            sum(min_x < x < max_x for x in x_gaps)

        min_y = min(y1, y2)
        max_y = max(y1, y2)
        y_dist = abs(y2 - y1) + (gap - 1) * \
            sum(min_y < y < max_y for y in y_gaps)

        total += x_dist + y_dist

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
GAP = 100
EXPECTED = 8410


@pytest.mark.parametrize(
    ('input_s', 'gap', 'expected'),
    (
        (INPUT_S, GAP, EXPECTED),
    ),
)
def test(input_s: str, gap: int, expected: int) -> None:
    assert solve(input_s, gap) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(solve(f.read(), 1000000))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
