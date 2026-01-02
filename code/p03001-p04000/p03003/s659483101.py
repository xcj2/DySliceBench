#!/usr/bin/env python3
import sys
INF = float("inf")
MOD = 1000000007  # type: int


def solve(N: int, M: int, S: "List[int]", T: "List[int]"):

    DP = [[1]*(N+1) for _ in range(M+1)]
    for j in range(1, M+1):
        for i in range(1, N+1):
            DP[j][i] = DP[j-1][i] + DP[j][i-1] - \
                DP[j-1][i-1]
            DP[j][i] %= MOD

            if S[i-1] == T[j-1]:
                DP[j][i] += DP[j-1][i-1]
                DP[j][i] %= MOD
    # print(*DP, sep="\n")
    print(DP[M][N])


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    T = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, S, T)


if __name__ == '__main__':
    main()
