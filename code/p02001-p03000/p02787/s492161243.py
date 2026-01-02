#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(H: int, N: int, A: "List[int]", B: "List[int]"):
    dp = [[INF] * (H+1) for i in range(N+1)]

    for i in range(1,N+1):
        for j in range(1, H+1):
            if j-A[i-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-A[i-1]]+B[i-1])
            else:
                dp[i][j] = min(dp[i-1][j], B[i-1])

    # for i in dp:
    #     print(i)
    print(dp[N][H])
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
