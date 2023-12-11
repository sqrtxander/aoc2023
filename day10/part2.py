from __future__ import annotations

import argparse
import os.path

import pytest

import support

import heapq

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.in')


def solve(s: str) -> int:
    def dijkstra(x: int, y: int) -> int:
        pq = [((0, x, y))]
        heapq.heapify(pq)
        dists = {}
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
    width = len(lines[0])
    height = len(lines)

    pipes[(sx, sy)] = get_start()

    seen = set()
    dijkstra(sx, sy)
    for x in range(width):
        for y in range(height):
            if (x, y) not in seen:
                pipes[(x, y)] = '.'

    total = 0
    for x in range(width):
        for y in range(height):
            if (x, y) in seen:
                continue
            left_ups = sum(pipes.get((ox, y), '.') in '|7F' for ox in range(x))
            if left_ups % 2 != 0:
                total += 1

    return total


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
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L
'''
EXPECTED = 10


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
