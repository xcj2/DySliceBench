#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    base = w[0]
    max_w = 3 * N
    dp = [[-1] * (max_w + 1)  for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(N, -1, -1):
            for k in range(max_w, -1, -1):
                if dp[j][k] >= 0:
                    dp[j + 1][k + w[i] - base] = max(dp[j + 1][k + w[i] - base], dp[j][k] + v[i])
    ret = 0
    for j in range(N + 1):
        for k in range(max_w + 1):
            if base * j + k <= W:
                ret = max(ret, dp[j][k])
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
