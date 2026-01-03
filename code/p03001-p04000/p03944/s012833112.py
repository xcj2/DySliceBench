#!/usr/bin/env python3
import sys
from bisect import bisect_left
INF = float("inf")


def solve(W: int, H: int, N: int, x: "List[int]", y: "List[int]", a: "List[int]"):
    X = [[0], [W], [0], [H]]
    for i in range(N):
        b = a[i]-1
        if b == 0 or b == 1:
            X[b].append(x[i])
        else:
            X[b].append(y[i])
    lower_x = max(X[0])
    upper_x = min(X[1])
    lower_y = max(X[2])
    upper_y = min(X[3])

    area = max(upper_x-lower_x, 0)*max(upper_y-lower_y, 0)
    print(area)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    a = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        a[i] = int(next(tokens))
    solve(W, H, N, x, y, a)


if __name__ == '__main__':
    main()
