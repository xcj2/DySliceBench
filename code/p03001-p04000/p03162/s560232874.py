#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, a: "List[int]", b: "List[int]", c: "List[int]"):
    v = [a, b, c]
    dp = [[0] * 3 for _ in range(N + 1)]
    dp[1] = [a[0], b[0], c[0]]
    for i in range(1, N):
        for j in range(3):
            for k in [1, 2]:
                dp[i + 1][j] = max(dp[i + 1][j], dp[i][(j + k) % 3] + v[j][i])
    print(max(dp[N]))
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]" 
    b = [int()] * (N)  # type: "List[int]" 
    c = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(N, a, b, c)

if __name__ == '__main__':
    main()
