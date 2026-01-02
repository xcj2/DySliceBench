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
    arr = read_v(n)

    max_asc = [0]
    for a in arr[:n - 1]:
        max_asc.append(max(max_asc[-1], a))
    #  print(max_asc)

    max_desc = [0]
    for a in arr[::-1][:n - 1]:
        max_desc.append(max(max_desc[-1], a))
    max_desc = max_desc[::-1]
    #  print(max_desc)

    #  assert len(max_asc) == len(max_desc)
    #  print(len(max_asc))

    for a, d in zip(max_asc, max_desc):
        print(max(a, d))


if __name__ == '__main__':
    main()
