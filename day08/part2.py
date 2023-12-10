from __future__ import annotations

import argparse
import os.path

import pytest

import support

from itertools import cycle
from functools import reduce
from math import lcm
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    # This only works because Eric was nice and made each starting point a
    # cycle to the end
    def count_steps(pos: str) -> int:
        count = 0
        for choice in cycle(order):
            pos = maps[pos][1 if choice == 'R' else 0]
            count += 1
            if pos.endswith('Z'):
                break

        return count
    order, lines = s.split('\n\n')
    maps = {}
    for line in lines.splitlines():
        a, b = line.split(' = ')
        maps[a] = b[1:-1].split(', ')

    steps = [count_steps(pos) for pos in maps if pos.endswith('A')]
    return lcm(*steps)


INPUT_S = '''\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
'''
EXPECTED = 6


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
