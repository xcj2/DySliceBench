#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)

# Override `input` function because `stdin.readline()` is 10x faster than built-in `input()`
input = sys.stdin.readline


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    a, b, c = read_h()

    mod = set((a * i) % b for i in range(1, b + 1))
    if c in mod:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
