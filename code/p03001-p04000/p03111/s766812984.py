#!/usr/bin/env python3
from itertools import product
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: int, B: int, C: int, l: "List[int]"):
    m = None
    for p in product(range(4), repeat=N):
        a = {i for i in range(N) if p[i] == 0}
        b = {i for i in range(N) if p[i] == 1}
        c = {i for i in range(N) if p[i] == 2}
        if not a or not b or not c:
            continue
        md = (
            abs(sum(l[ai] for ai in a) - A) + 10 * (len(a) - 1) +
            abs(sum(l[bi] for bi in b) - B) + 10 * (len(b) - 1) +
            abs(sum(l[ci] for ci in c) - C) + 10 * (len(c) - 1)
        )
        if m is None or m > md:
            m = md

    print(m)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    l = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B, C, l)


if __name__ == '__main__':
    main()
