#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, l: "List[int]", r: "List[int]"):
    print(sum(ri - li + 1 for li, ri in zip(l, r)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    l = [int()] * (N)  # type: "List[int]"
    r = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        l[i] = int(next(tokens))
        r[i] = int(next(tokens))
    solve(N, l, r)


if __name__ == '__main__':
    main()
