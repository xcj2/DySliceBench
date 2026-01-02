#!/usr/bin/env python3
import sys

def solve(N, M, A, B, C):
    key = []  # type: "List[List[int, int]]"
    for i in range(M):
        s = 0
        for j in range(B[i]):
            s |= 1 << (C[i][j] - 1)
        key.append([s, A[i]])
    
    INF = 1001001001
    dp = [INF] * (1 << N)
    dp[0] = 0
    for s in range(1 << N):
        for i in range(M):
            t = s | key[i][0]
            cost = dp[s] + key[i][1]
            dp[t] = min(dp[t], cost)
    ans = dp[-1]
    print(-1 if ans == INF else ans)
    pass


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A, B, C = [], [], []
    for _  in range(M):
        A.append(int(next(tokens)))
        B.append(int(next(tokens)))
        C.append([int(next(tokens)) for _ in range(B[-1])])
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
