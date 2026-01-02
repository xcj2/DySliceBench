#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, T: int, c: "List[int]", t: "List[int]"):
    try:
        print(min(ci for ci, ti in zip(c, t) if ti <= T))
    except ValueError:
        print("TLE")


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    c = [int()] * (N)  # type: "List[int]"
    t = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        c[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, T, c, t)


if __name__ == '__main__':
    main()
