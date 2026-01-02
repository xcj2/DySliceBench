#!/usr/bin/env python3
import sys
import math
INF = float("inf")


def solve(N: str, K: int):
    M = len(N)
    DP = [[[0]*2 for __ in range(K+1)] for _ in range(M+1)]
    Nstr = N

    DP[0][0][False] = 1

    for i in range(M):
        DP[i+1][0][True] = 1
        DP[i+1][0][False] = 0
        for k in range(K):
            DP[i+1][k+1][True] = DP[i][k][True]*9 + DP[i][k+1][True]*1
            if int(Nstr[i]) != 0:
                DP[i+1][k+1][True] += DP[i][k+1][False]
                DP[i+1][k+1][True] += DP[i][k][False]*(int(Nstr[i])-1)
            if int(Nstr[i]) == 0:
                DP[i+1][k+1][False] = DP[i][k+1][False]
            else:
                DP[i+1][k+1][False] = DP[i][k][False]
    print(DP[M][K][True]+DP[M][K][False])
    # print(*DP, sep="\n")

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = str(next(tokens))  #
    K = int(next(tokens))  # type: int
    solve(N, K)


if __name__ == '__main__':
    main()
