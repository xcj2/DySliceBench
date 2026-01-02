#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def paintable(H, W, S, i, j):
    return (i - 1 >= 0 and S[i - 1][j] == '#') or (i + 1 <= H - 1 and S[i + 1][j] == '#') or (
        j - 1 >= 0 and S[i][j - 1] == '#') or (j + 1 <= W - 1 and S[i][j + 1] == '#')


def main():
    H, W = read_h()
    S = read_v(H, typ=str)

    for i, row in enumerate(S):
        for j, c in enumerate(row):
            if c == '.':
                continue

            if not paintable(H, W, S, i, j):
                print('No')
                return

    print('Yes')


if __name__ == '__main__':
    main()
