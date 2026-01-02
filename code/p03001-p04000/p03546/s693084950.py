#!/usr/bin/env pypy3

import itertools

NUM_TYPES = 10
INVALID = -1


def in_place_min_costs(min_dist, num_vs=NUM_TYPES):
    for k, i, j in itertools.product(range(num_vs), repeat=3):
        min_dist[i][j] = min(min_dist[i][j], min_dist[i][k] + min_dist[k][j])


def solve(h, w, cs, board):
    in_place_min_costs(cs)
    res = 0
    for i, j in itertools.product(range(h), range(w)):
        b = board[i][j]
        if b != INVALID:
            res += cs[b][1]
    return res


def main():
    h, w = (int(x) for x in input().split())
    cs = [[int(x) for x in input().split()] for _ in range(NUM_TYPES)]
    board = [[int(x) for x in input().split()] for _ in range(h)]
    res = solve(h, w, cs, board)
    print(res)


if __name__ == '__main__':
    main()
