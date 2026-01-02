#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h() if m > 1 else typ(input()) for _ in range(n)]


def cell(c, H, W, S, i, j):
    if c == '#':
        return c

    return sum([
        int(i - 1 >= 0 and S[i - 1][j] == '#'),
        int(j + 1 <= W - 1 and S[i][j + 1] == '#'),
        int(i + 1 <= H - 1 and S[i + 1][j] == '#'),
        int(j - 1 >= 0 and S[i][j - 1] == '#'),
        int(i - 1 >= 0 and j - 1 >= 0 and S[i - 1][j - 1] == '#'),
        int(i - 1 >= 0 and j + 1 <= W - 1 and S[i - 1][j + 1] == '#'),
        int(i + 1 <= H - 1 and j + 1 <= W - 1 and S[i + 1][j + 1] == '#'),
        int(i + 1 <= H - 1 and j - 1 >= 0 and S[i + 1][j - 1] == '#'),
    ])


def main():
    H, W = read_h()
    S = read_v(H, typ=str)

    for i, row in enumerate(S):
        ans_row = ''.join([str(cell(c, H, W, S, i, j)) for j, c in enumerate(row)])
        print(ans_row)


if __name__ == '__main__':
    main()
