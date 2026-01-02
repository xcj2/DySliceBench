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
    A = read_h()
    B = read_h()

    ans = 0
    rem_cap = 0
    for a, b in zip(A, B):
        cap = rem_cap + b
        if a >= cap:
            ans += cap
            rem_cap = 0
        elif rem_cap >= a:
            ans += a
            rem_cap = b
        else:
            ans += a
            rem_cap = cap - a

        #  print('killed:', ans)
        #  print('remaining:', rem_cap)

    if rem_cap >= A[-1]:
        ans += A[-1]
    else:
        ans += rem_cap

    print(ans)


if __name__ == '__main__':
    main()
