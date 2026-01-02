#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, W: "List[int]"):
    s2 = sum(W)
    s1 = 0
    m = s2
    for Wi in W[:-1]:
        s1 += Wi
        s2 -= Wi
        m = min(m, abs(s1 - s2))
    print(m)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, W)


if __name__ == '__main__':
    main()
