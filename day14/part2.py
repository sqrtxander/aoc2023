from __future__ import annotations

import argparse
import os.path

import pytest

import support

from functools import cache
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    rocks = tuple(tuple(l) for l in s.splitlines())
    grid_times = {}
    cycles = 1000000000
    i = 0
    while i < cycles:
        rocks = cycle(rocks)
        if rocks in grid_times:
            diff = i - grid_times[rocks]
            i += (cycles - i) // diff * diff
        grid_times[rocks] = i
        i += 1
    return score(rocks)


@cache
def cycle(rocks: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    for _ in range(4):
        rocks = rotate_clockwise(rocks)
        rocks = slide_right(rocks)
    return rocks


def slide_right(rocks: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    new_rocks = []
    for col in rocks:
        col_s = ''.join(col)
        while 'O.' in col_s:
            col_s = col_s.replace('O.', '.O')
        new_rocks.append(tuple(col_s))

    return tuple(new_rocks)


def rotate_clockwise(rocks: tuple[tuple[str, ...], ...]) -> tuple[tuple[str, ...], ...]:
    return tuple(zip(*rocks[::-1]))


def score(rocks: tuple[tuple[str, ...], ...]) -> int:
    total = 0
    i = len(rocks)
    for row in rocks:
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
EXPECTED = 64


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
