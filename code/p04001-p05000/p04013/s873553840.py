#!/usr/bin/env python3
import sys
try:
    from typing import List
except ImportError:
    pass


def solve(N: int, A: int, x: "List[int]"):
    dp = [[0] * (A * N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    for xi in x:
        for k in reversed(range(1, N + 1)):
            for j in range(xi, A * N + 1):
                if j >= xi:
                    dp[k][j] += dp[k - 1][j - xi]
    print(sum(dp[i][A * i] for i in range(1, N + 1)))


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, x)


if __name__ == '__main__':
    main()
