#!/usr/bin/env python3
import sys
from pprint import pprint

MOD = 1000000007  # type: int

def solve(N: int, M: int, S: "List[int]", T: "List[int]"):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        dp[i][0] = 1
    for j in range(M + 1):
        dp[0][j] = 1
    for i in range(N):
        for j in range(M):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1]
            if not S[i] == T[j]:
                dp[i + 1][j + 1] -= dp[i][j]
            dp[i + 1][j + 1] %= MOD
    #pprint(dp)
    ret = dp[N][M]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = [ int(next(tokens)) for _ in range(N) ]  # type: "List[int]"
    T = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, S, T)

if __name__ == '__main__':
    main()
