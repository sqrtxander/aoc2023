from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    chunks = s.split('\n\n')
    total = 0
    for chunk in chunks:
        pattern = tuple(tuple(line) for line in chunk.splitlines())

        h = horizontal(pattern)
        if h != 0:
            total += 100 * h
            continue

        v = horizontal(list(zip(*pattern)))
        assert v != 0
        total += v

    return total


def horizontal(pattern):
    for i, (l1, l2) in enumerate(zip(pattern, pattern[1:]), start=1):
        if l1 == l2 and check(pattern, i):
            return i

    return 0


def check(pattern, ref_idx):
    for i in range(max(2 * ref_idx - len(pattern), 0), ref_idx):
        if pattern[i] != pattern[2 * ref_idx - i - 1]:
            return False

    return True


INPUT_S = '''\
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
'''
EXPECTED = 405


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
