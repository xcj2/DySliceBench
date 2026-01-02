#!/usr/bin/env python3
import sys


def solve(x: "List[int]", y: "List[int]"):
    base = [x[1]-x[0], y[1]-y[0]]
    x3, y3 = [x[1]-base[1], y[1] + base[0]]
    x4, y4 = [x3-base[0], y3-base[1]]
    # x4 = x[0] + y[0]-y[1]
    # y4 = y[0] - x[0]-x[1]
    print(*[x3, y3, x4, y4])
    return


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
