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
    S, = read_h(typ=str)
    n = len(S) - 1

    total = 0
    for i in range(2**n):
        prev = 0
        for j in range(n):
            #  print(i, j)
            if ((i >> j) & 1):
                #  print(i, j)
                m = int(S[prev:j + 1])
                #  print(m)
                total += m
                prev = j + 1

        m = int(S[prev:])
        #  print(m)
        total += m

    print(total)


if __name__ == '__main__':
    main()
