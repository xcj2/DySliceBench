#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, x: "List[int]", y: "List[int]", h: "List[int]"):
    for cx in range(101):
        for cy in range(101):
            chs = {
                hi + abs(xi - cx) + abs(yi - cy)
                for xi, yi, hi in zip(x, y, h)
                if hi != 0
            }
            if len(chs) != 1:
                continue
            ch, = chs
            if any(max(ch - abs(xi - cx) - abs(yi - cy), 0) != hi
                   for xi, yi, hi in zip(x, y, h)):
                print(cx, cy, ch, file=sys.stderr)
                continue
            print(cx, cy, ch)
            return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    h = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        h[i] = int(next(tokens))
    solve(N, x, y, h)


if __name__ == '__main__':
    main()
