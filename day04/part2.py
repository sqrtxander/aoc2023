from __future__ import annotations

import argparse
import os.path

import pytest

import support
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    lines = s.splitlines()
    won = {card: 1 for card in range(1, len(lines) + 1)}

    for line in lines:
        card_s, nums = line.split(': ')
        card = int(card_s.split()[-1])

        winning_s, my_s = nums.split(' | ')
        winning = [int(num) for num in winning_s.split()]
        my = [int(num) for num in my_s.split()]

        matches = 0
        for num in my:
            if num in winning:
                matches += 1

        for c in range(card + 1, card + matches + 1):
            if c > len(lines):
                break
            won[c] += won[card]

    return sum(won.values())


INPUT_S = '''\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
'''
EXPECTED = 30


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
