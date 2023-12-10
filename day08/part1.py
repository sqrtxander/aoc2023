from __future__ import annotations

import argparse
import os.path

import pytest

import support

from itertools import cycle
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    order, lines = s.split('\n\n')
    maps = {}
    for line in lines.splitlines():
        a, b = line.split(' = ')
        maps[a] = b[1:-1].split(', ')

    pos = 'AAA'
    count = 0
    for choice in cycle(order):
        pos = maps[pos][1 if choice == 'R' else 0]
        count += 1
        if pos == 'ZZZ':
            return count


INPUT_S = '''\
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
'''
EXPECTED = 2


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
