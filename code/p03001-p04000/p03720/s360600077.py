#!/usr/bin/env python3
from collections import Counter
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    c = Counter(a + b)
    for i in range(1, N + 1):
        print(c[i])


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int()] * (M)  # type: "List[int]"
    b = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, M, a, b)


if __name__ == '__main__':
    main()
