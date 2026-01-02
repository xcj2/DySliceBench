#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)
 
 
def solve(N: int, K: int, h: "List[int]"):
    INF = float('inf')
    dp = [INF] * N
    dp[0] = 0
    for i in range(N):
        for j in range(K):
            if i + j + 1 < N:
                dp[i + j + 1] = min(dp[i + j + 1], dp[i] + abs(h[i + j + 1] - h[i]))
    print(dp[N - 1])
    return
 
 
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    h = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    solve(N, K, h)
 
if __name__ == '__main__':
    main()