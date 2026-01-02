#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, t: "List[int]", x: "List[int]", y: "List[int]"):
    pti = 0
    pxi = 0
    pyi = 0
    for ti, xi, yi in zip(t, x, y):
        dt = ti - pti
        dx = xi - pxi
        dy = yi - pyi
        if abs(dx) + abs(dy) > dt or (dx + dy + dt) % 2 != 0:
            print(NO)
            return
        pti = ti
        pxi = xi
        pyi = yi
    print(YES)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]"
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, t, x, y)


if __name__ == '__main__':
    main()
