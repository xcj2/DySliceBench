#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, h: "List[int]"):
    INF = float('inf')
    dp = [INF] * N
    dp[0] = 0
    for i in range(N - 1):
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(h[i + 1] - h[i]))
        if i < N - 2:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(h[i + 2] - h[i]))
    print(dp[N - 1])
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, h)

if __name__ == '__main__':
    main()
