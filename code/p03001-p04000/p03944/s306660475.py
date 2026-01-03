#!/usr/bin/env python3
import sys
import numpy as np

def solve(W: int, H: int, N: int, x: "List[int]", y: "List[int]", a: "List[int]"):
    grid = np.zeros((H,W))
    for i in range(N):
        if a[i] == 1:
            grid[:,:x[i]] = 1
        elif a[i] == 2:
            grid[:,x[i]:] = 1
        elif a[i] == 3:
            grid[:y[i],:] = 1
        elif a[i] == 4:
            grid[y[i]:,:] = 1
    print(np.count_nonzero(grid==0))
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
