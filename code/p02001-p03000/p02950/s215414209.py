#!/usr/bin/env python3
import sys
import functools
INF = float("inf")


def solve(p: int, a: "List[int]"):
    N = p+1
    MOD = p

    inv = [0]*N
    inv[1] = 1
    for i in range(2, N):
        inv[i] = -inv[MOD % i]*(MOD//i) % MOD

    b = [0]*p
    for ai, av in enumerate(a):
        if av == 0:
            continue

        c = 1
        d = 1
        for i in range(p-1, -1, -1):
            b[i] += - c * d
            b[i] %= p
            c = c * i * inv[p-i] % p
            d = -d*ai % p
        b[0] += 1
        b[0] %= p
    print(*b, sep=" ")
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    p = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(p-1-0+1)]  # type: "List[int]"
    solve(p, a)


if __name__ == '__main__':
    main()
