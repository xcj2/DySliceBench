#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10**7)

input = sys.stdin.readline


def read_h(typ=int):
    return list(map(typ, input().split()))


def read_v(n, m=1, typ=int):
    return [read_h(typ) if m > 1 else typ(input()) for _ in range(n)]


def main():
    n, = read_h()
    arr = read_h()

    s = [0] * (n + 1)
    for i, a in enumerate(arr):
        k = s[i] + a
        s[i + 1] = k
    #  print(s)

    cnts = {}
    for si in s:
        cnts[si] = cnts.get(si, 0) + 1
    #  print(cnts)

    ans = sum([cnt * (cnt - 1) // 2 for cnt in cnts.values()])
    print(ans)


if __name__ == '__main__':
    main()
