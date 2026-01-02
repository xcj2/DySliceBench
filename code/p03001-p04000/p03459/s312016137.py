#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, t, x, y):
    ct = 0
    cx = 0
    cy = 0
    for i in range(N):
        r = t[i] - ct - abs(cx - x[i]) - abs(cy - y[i])
        if r < 0 or r & 1:
            return NO
        ct = t[i]
        cx = x[i]
        cy = y[i]
    return YES


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
    print(solve(N, t, x, y))

if __name__ == '__main__':
    main()
