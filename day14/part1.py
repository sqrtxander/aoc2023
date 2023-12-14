from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    rocks = s.splitlines()
    new_rocks = []
    for col in zip(*rocks):
        col_s = ''.join(col)
        while '.O' in col_s:
            col_s = col_s.replace('.O', 'O.')
        new_rocks.append(tuple(col_s))

    new_rocks = tuple(zip(*new_rocks))

    total = 0
    i = len(new_rocks)
    for row in new_rocks:
        total += i * row.count('O')
        i -= 1
    return total


INPUT_S = '''\
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
'''
EXPECTED = 136


@ pytest.mark.parametrize(
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
