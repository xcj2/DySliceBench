#!/usr/bin/env python3
import sys
INF = float("inf")


def solve(N: int, T: int, A: "List[int]", B: "List[int]"):

    # DP1
    # 1からi番目の料理でj分以内に完食できる美味しさの合計の最大値
    DP1 = [[0 for _ in range(T+1)] for __ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, T+1):
            if j-A[i-1] >= 0:
                DP1[i][j] = max(DP1[i][j], DP1[i-1][j-A[i-1]]+B[i-1])
            DP1[i][j] = max(DP1[i][j], DP1[i-1][j], DP1[i][j-1])

    # DP2
    # i番目からN番目の料理でj分以内に完食できる美味しさの合計の最大値
    DP2 = [[0 for _ in range(T+1)] for __ in range(N+2)]
    for i in range(N, 0, -1):
        for j in range(1, T+1):
            if j-A[i-1] >= 0:
                DP2[i][j] = max(DP2[i][j], DP2[i+1][j-A[i-1]]+B[i-1])
            DP2[i][j] = max(DP2[i][j], DP2[i+1][j], DP2[i][j-1])

    # i番目以外の料理でT-1分以内に完食できる美味しさの合計の最大値
    ans = 0
    for i in range(1, N+1):
        bns = 0
        for j in range(T):
            bns = max(bns, DP1[i-1][j] + DP2[i+1][T-j-1])
        ans = max(ans, bns+B[i-1])
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
