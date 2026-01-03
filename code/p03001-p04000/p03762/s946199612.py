#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


def solve(n: int, m: int, x: "List[int]", y: "List[int]"):

    xtot = 0
    for i in range(n-1):
        xtot += (x[i+1]-x[i])*(i+1)*(n-i-1) % MOD
    ytot = 0
    for i in range(m-1):
        ytot += (y[i+1]-y[i])*(i+1)*(m-i-1) % MOD

    print(xtot*ytot % MOD)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(n)]  # type: "List[int]"
    y = [int(next(tokens)) for _ in range(m)]  # type: "List[int]"
    solve(n, m, x, y)


if __name__ == '__main__':
    main()
