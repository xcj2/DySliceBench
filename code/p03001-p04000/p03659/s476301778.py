#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, a: "List[int]"):
    s = sum(a)
    c = 0
    m = float("inf")
    for i in range(len(a) - 1):
        c += a[i]
        m = min(m, abs(2 * c - s))
    print(m)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)


if __name__ == '__main__':
    main()
