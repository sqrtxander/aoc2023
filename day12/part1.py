from __future__ import annotations

import argparse
import os.path

import pytest

import support

from functools import lru_cache
INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    total = 0
    lines = s.strip().splitlines()
    for line in lines:
        spring, nums_s = line.split(' ')
        criteria = tuple(int(num) for num in nums_s.split(','))
        total += count_ways(spring, criteria)

    return total


@lru_cache()
def count_ways(spring: string, criteria: tuple[int]) -> int:
    spring = spring.lstrip('.')

    if spring == '':
        return 1 if criteria == () else 0

    if criteria == ():
        return 1 if '#' not in spring else 0

    if spring[0] == '#':
        if len(spring) < criteria[0] or '.' in spring[:criteria[0]]:
            return 0

        if len(spring) == criteria[0]:
            return 1 if len(criteria) == 1 else 0

        if spring[criteria[0]] == '#':
            return 0

        else:
            return count_ways(spring[criteria[0] + 1:], criteria[1:])

    total = 0
    total += count_ways('#' + spring[1:], criteria)
    total += count_ways(spring[1:], criteria)

    return total


INPUT_S = '''\
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
'''
EXPECTED = 21


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
