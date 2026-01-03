#!/usr/bin/env python3
from itertools import permutations
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, M: int, a: "List[int]", b: "List[int]"):
    e = set(zip(a, b))
    print(sum(
        1 for p in permutations(range(2, N + 1))
        if all((n1, n2) in e or (n2, n1) in e for n1, n2 in zip((1,) + p, p))
    ))


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
