#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    INF = float('inf')
    MAX_V = 10 ** 3 * N
    dp = [INF] * (MAX_V + 1)
    dp[0] = 0
    for i in range(N):
        for j in range(MAX_V - v[i], -1, -1):
            dp[j + v[i]] = min(dp[j + v[i]], dp[j] + w[i])
    ret = 0
    for j in range(MAX_V + 1):
        if dp[j] <= W:
            ret = max(ret, j)
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]" 
    v = [int()] * (N)  # type: "List[int]" 
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)

if __name__ == '__main__':
    main()
