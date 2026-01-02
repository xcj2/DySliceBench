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
    mod = [None] + read_h()

    i = n
    box = [None] * (n + 1)
    while i >= 1:
        s = sum(box[j] for j in range(i * 2, n + 1, i))
        box[i] = abs(mod[i] - (s % 2))
        i -= 1

    #  print([i for i in range(n + 1)])
    #  print(box)

    print(sum(box[1:]))
    t = [str(i) for i, b in enumerate(box) if b is not None and b > 0]
    if t:
        print(' '.join(t))


if __name__ == '__main__':
    main()
