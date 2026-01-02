#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)
from itertools import permutations

def solve(N, M, a, b, c):
    MAX = 2 ** N - 1
    INF = float('inf')
    dp = [INF] * (2 ** N)
    dp[0] = 0
    for i in range(M):
        bits = 0
        for j in c[i]:
            bits += (1 << (j - 1))
        for b in range(2 ** N):
            dp[b | bits] = min(dp[b | bits], dp[b] + a[i])
    if dp[MAX] < INF:
        print(dp[MAX])
    else:
        print(-1)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = []
    b = []
    c = []
    for i in range(M):
        A = int(next(tokens))  # type: int
        B = int(next(tokens))  # type: int
        a.append(A)
        b.append(B)
        c.append([ int(next(tokens)) for _ in range(B) ])
    solve(N, M, a, b, c)


if __name__ == '__main__':
    main()
