#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(H: int, N: int, A: "List[int]", B: "List[int]"):
    dp = [float('inf')] * (H + 1)
    dp[0] = 0
    for i in range(N):
        for j in range(H + 1):
            tmp = min(H, j + A[i])
            dp[tmp] = min(dp[tmp], dp[j] + B[i])
    print(dp[H])
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(H, N, A, B)

if __name__ == '__main__':
    main()
