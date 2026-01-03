#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(W: int, H: int, N: int, x: "List[int]", y: "List[int]", a: "List[int]"):
    x0, x1 = 0, W
    y0, y1 = 0, H
    for i in range(N):
        if a[i] == 1:
            x0 = max(x0, x[i])
        if a[i] == 2:
            x1 = min(x1, x[i])
        if a[i] == 3:
            y0 = max(y0, y[i])
        if a[i] == 4:
            y1 = min(y1, y[i])
    if x1 <= x0 or y1 <= y0:
        ret = 0
    else:
        ret = (x1 - x0) * (y1 - y0)
    print(ret)
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
