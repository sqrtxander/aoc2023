from __future__ import annotations

import argparse
import os.path

import pytest

import support

import heapq
from collections import defaultdict

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    def dijkstra(x: int, y: int) -> int:
        pq = [((0, x, y))]
        heapq.heapify(pq)
        seen = set()
        dists = defaultdict(int)
        while pq:
            c, x, y = heapq.heappop(pq)
            if (x, y) in seen:
                continue

            seen.add((x, y))
            dists[(x, y)] = c

            for nx, ny in get_neighbours(x, y, pipes[(x, y)]):
                heapq.heappush(pq, (c + 1, nx, ny))

        return max(dists.values())

    def get_start() -> str:
        possible_chars = set('|-LJ7F.')
        u_char = pipes.get((sx, sy - 1), '.')
        r_char = pipes.get((sx + 1, sy), '.')
        d_char = pipes.get((sx, sy + 1), '.')
        l_char = pipes.get((sx - 1, sy), '.')

        if u_char in '|7F':
            possible_chars &= set('|LJ')
        if r_char in '-J7':
            possible_chars &= set('-LF')
        if d_char in '|LJ':
            possible_chars &= set('|7F')
        if l_char in '-LF':
            possible_chars &= set('-J7')

        assert len(possible_chars) == 1
        return possible_chars.pop()

    lines = s.splitlines()
    sx, sy = None, None
    pipes = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                sx, sy = x, y
            pipes[(x, y)] = char
    pipes[(sx, sy)] = get_start()
    return dijkstra(sx, sy)


def get_neighbours(x: int, y: int, char: str) -> tuple[tuple[int, int]]:
    if char == '|':
        check = ((0, -1), (0, 1))
    elif char == '-':
        check = ((-1, 0), (1, 0))
    elif char == 'L':
        check = ((0, -1), (1, 0))
    elif char == 'J':
        check = ((0, -1), (-1, 0))
    elif char == '7':
        check = ((0, 1), (-1, 0))
    elif char == 'F':
        check = ((0, 1), (1, 0))
    elif char == '.':
        check = ()
    return ((x + dx, y + dy) for dx, dy in check)


INPUT_S = '''\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
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
