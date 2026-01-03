#!/usr/bin/env python3
import sys

def solve(N: int, A: int, x: "List[int]"):
    ## dp[i][j][k] = i番目までのカードからjマイ選んで合計kにする選び方の総数
    dp = [[[0]*2501 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(N):
        dp[i][0][0] = 1

    for i in range(N):
        for j in range(N):
            for k in range(2501):
                if k-x[i] >= 0:
                    dp[i+1][j+1][k] = dp[i][j][k-x[i]]+dp[i][j+1][k]
                else:
                    dp[i+1][j+1][k] = dp[i][j+1][k]

    answer = 0
    for j in range(1,N+1):
        answer += dp[N][j][A*j]
    print(answer)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, x)

if __name__ == '__main__':
    main()
