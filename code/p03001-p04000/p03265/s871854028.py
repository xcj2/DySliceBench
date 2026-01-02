#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(x: "List[int]", y: "List[int]"):
    x1, x2 = x
    y1, y2 = y
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x3 - (y3 - y2)
    y4 = y3 + (x3 - x2)
    print(x3, y3, x4, y4)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = [int()] * (2)  # type: "List[int]"
    y = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(x, y)


if __name__ == '__main__':
    main()
