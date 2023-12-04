from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')
MAX_PULL = {'red': 12,
            'green': 13,
            'blue': 14,
            }


def solve(s: str) -> int:
    possible_sum = 0
    lines = s.splitlines()
    for line in lines:
        game_s, info = line.split(': ')
        game = int(game_s.split()[-1])
        for round in info.split('; '):
            for pull in round.split(', '):
                num_s, col = pull.split()
                possible = True
                if int(num_s) > MAX_PULL[col]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_sum += game

    return possible_sum


INPUT_S = '''\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
'''
EXPECTED = 8


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
