from __future__ import annotations

import argparse
import os.path

import pytest

import support

from collections import Counter
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    def get_ranking(hand: str) -> int:
        occs = Counter(hand)
        if 5 in occs.values():  # 5
            value = 0
        elif 4 in occs.values():  # 4
            value = 1
        elif 3 in occs.values() and 2 in occs.values():
            value = 2
        elif 3 in occs.values():
            value = 3
        elif list(occs.values()).count(2) == 2:
            value = 4
        elif 2 in occs.values():
            value = 5
        else:
            value = 6

        for c in hand:
            value = 100 * value + rankings.index(c)
        return value

    rankings = list('AKQJT98765432')
    hands = [line.split() for line in s.splitlines()]
    hands.sort(key=lambda l: get_ranking(l[0]), reverse=True)
    total = 0
    for i, (_, bid_s) in enumerate(hands, start=1):
        total += i * int(bid_s)

    return total


INPUT_S = '''\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''
EXPECTED = 6440


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
