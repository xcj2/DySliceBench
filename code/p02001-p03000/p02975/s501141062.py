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
    n, = read_h()
    arr = read_h()
    #  print(arr)

    s = 0
    for a in arr:
        s ^= a

    if s == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
