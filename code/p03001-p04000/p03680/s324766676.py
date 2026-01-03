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
    nxt = [i - 1 for i in read_v(n)]

    idx = 0
    cnt = 0
    for _ in range(n):
        cnt += 1
        idx = nxt[idx]
        if idx == 1:
            print(cnt)
            return

    print(-1)


if __name__ == '__main__':
    main()
