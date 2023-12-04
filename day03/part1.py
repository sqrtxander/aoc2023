from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    coords = {}
    lines = s.splitlines()
    for y, line in enumerate(s.splitlines()):
        for x, c in enumerate(line):
            coords[(x, y)] = c
    width = len(lines[0])
    height = len(lines)

    total = 0
    x = 0
    for y in range(height):
        x = 0
        while x < width:
            if coords[(x, y)].isdigit():
                num_s = ''
                length = 0
                while coords.get((x + length, y), '.').isdigit():
                    num_s += coords.get((x + length, y), '.')
                    length += 1

                for neighbour in get_neighbours(x, y, length):
                    if coords.get(neighbour, '.') != '.' and not coords.get(neighbour, '.').isdigit():
                        total += int(num_s)
                        break
                x += length
            else:
                x += 1

    return total


def get_neighbours(x: int, y: int, l: int) -> Generator[Tuple[int, int], None, None]:
    for dx in range(-1, l + 1):
        for dy in range(-1, 2):
            if dy != 0 or dx not in range(l):
                yield (x + dx, y + dy)


INPUT_S = '''\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''
EXPECTED = 4361


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
