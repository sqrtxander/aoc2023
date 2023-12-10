from __future__ import annotations

import argparse
import os.path

import pytest

import support

from math import prod

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    time_s, dist_s = s.replace(' ', '').splitlines()
    time = int(time_s.split(':')[1])
    dist = int(dist_s.split(':')[1])

    winning = False
    count = 0
    for secs in range(time + 1):
        my_dist = secs * (time - secs)
        if my_dist > dist:
            winning = True
            count += 1
        elif my_dist <= dist and winning:
            break

    return count


INPUT_S = '''\
Time:      7  15   30
Distance:  9  40  200
'''
EXPECTED = 71503


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
