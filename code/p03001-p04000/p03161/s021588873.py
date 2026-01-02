#!/usr/bin/env python3
import sys

def min(val: int, new: int):
    if new < val:
        return new
    else:
        return val

def solve(N: int, K: int, h: "List[int]"):
    dp = [sys.maxsize] * N
    dp[0] = 0

    for i in range(1,N):
        for j in range(1,K+1):
            if i-j >= 0:
                dp[i] = min(dp[i],dp[i-j] + abs(h[i]-h[i-j]))

    print(dp[N-1])

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, h)

if __name__ == '__main__':
    main()