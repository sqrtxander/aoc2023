from __future__ import annotations

import argparse
import os.path

import pytest

import support

from math import prod

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    lines = s.splitlines()
    times = [int(t) for t in lines[0].split()[1:]]
    dists = [int(d) for d in lines[1].split()[1:]]

    total = 1
    for dist, time in zip(dists, times):
        winning = False
        count = 0
        for secs in range(time + 1):
            my_dist = secs * (time - secs)
            if my_dist > dist:
                winning = True
                count += 1
            elif my_dist <= dist and winning:
                total *= count
                break

    return total

INPUT_S = '''\
Time:      7  15   30
Distance:  9  40  200
'''
EXPECTED = 288


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
