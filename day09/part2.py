from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:

    lines = s.splitlines()
    total = 0
    for line in lines:
        nums = [int(num) for num in line.split()]
        sequences = [nums]
        while not all(h == 0 for h in sequences[-1]):
            sequences.append(
                [b - a for a, b in zip(sequences[-1], sequences[-1][1:])])

        num = 0
        for seq in sequences[::-1]:
            num = seq[0] - num
        total += num
    return total


INPUT_S = '''\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
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
