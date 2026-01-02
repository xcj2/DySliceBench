#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def solve(H: int, W: int, a: "List[List[str]]"):
    grid = [[0]*W for _ in range(H)]

    grid[0][0] = 1
    for i in range(H):
        for j in range(W):
            if a[i][j] == "#":
                continue
            if i > 0:
                grid[i][j] += grid[i-1][j]
                grid[i][j] %= MOD
            if j > 0:
                grid[i][j] += grid[i][j-1]
                grid[i][j] %= MOD
    print(grid[H-1][W-1])
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [next(tokens) for _ in range(H)]
    solve(H, W, a)


if __name__ == '__main__':
    main()
