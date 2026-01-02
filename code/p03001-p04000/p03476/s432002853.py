#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def is_prime(n: int):
    if n == 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def solve(Q: int, l: "List[int]", r: "List[int]"):
    pm = [is_prime(n) for n in range(1, 100001, 2)]
    tm = [
        pm[(n - 1) // 2] and (
            n == 3 or
            ((n + 1) // 2 % 2 == 1 and pm[((n + 1) // 2 - 1) // 2])
        )
        for n in range(1, 100001, 2)
    ]
    acc = [0] * (len(tm) + 1)
    for i in range(len(tm)):
        acc[i + 1] = acc[i] + int(tm[i])
    for li, ri in zip(l, r):
        print(acc[(ri - 1) // 2 + 1] - acc[(li - 1) // 2])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    l = [int()] * (Q)  # type: "List[int]"
    r = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(Q, l, r)


if __name__ == '__main__':
    main()
