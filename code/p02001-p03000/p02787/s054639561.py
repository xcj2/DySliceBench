#!/usr/bin/env python3
import sys


def solve(H: int, N: int, A: "List[int]", B: "List[int]"):
    # AB = sorted(list(zip(A,B)),key=lambda x: -x[0]/x[1])

    # dp[i][j] i番目までの技からいくつか選んで体力H以下にするときの最小MP

    dp = [[10**9]*(H+10**4+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 0

    for i in range(N):
        for h in range(H+10**4+1):
            if h - A[i] >= 0:
                dp[i+1][h] = min(dp[i+1][h-A[i]]+B[i],dp[i][h])
            else:
                dp[i+1][h] = dp[i][h]
 

    answer = 10**9
    for i in range(H,H+10**4+1):
        answer = min(answer,dp[-1][i])
    print(answer)
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
