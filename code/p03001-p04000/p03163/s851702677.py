#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)


def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j + w[i] <= W:
                dp[j + w[i]] = max(dp[j + w[i]], dp[j] + v[i])
    ret = max(dp)
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
