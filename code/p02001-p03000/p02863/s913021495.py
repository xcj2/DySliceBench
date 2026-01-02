#!/usr/bin/env python3
import sys


def solve(N: int, T: int, A: "List[int]", B: "List[int]"):
    # dp[i][w][超えたか超えてないか超えたら1]:= (i番目までの品物の中から重さが w を超えないように選んだときの、価値の総和の最大値,[index])

    AB = list(zip(A,B))
    AB.sort(key=lambda x:x[0])
    A = [AB[i][0] for i in range(N)]
    B = [AB[i][1] for i in range(N)]

    dp  = [[0 for _ in range(T)] for _ in range(N+1)]
    ans = 0
    for i in range(N):
        ans = max(ans,dp[i][T-1]+B[i])

        for j in range(0,T):

            if j >= A[i]: ##今回の商品がjよりも小さい
                dp[i+1][j] = max(dp[i][j-A[i]]+B[i],dp[i][j])
            else: ## 選ばない
                dp[i+1][j] = dp[i][j]
             
    print(ans)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, T, A, B)

if __name__ == '__main__':
    main()
