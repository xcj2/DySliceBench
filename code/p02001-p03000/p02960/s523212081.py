#!/usr/bin/env python3
import sys
sys.setrecursionlimit(300000)

MOD = 1000000007  # type: int

def solve(S: str):
    N = len(S)
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(13):
            if S[i] == '?':
                for k in range(10):
                    nex = (j * 10 + k) % 13
                    dp[i + 1][nex] += dp[i][j]
                    dp[i + 1][nex] %= MOD
            else:
                k = int(S[i])
                nex = (j * 10 + k) % 13
                dp[i + 1][nex] += dp[i][j]
                dp[i + 1][nex] %= MOD
    ret = dp[N][5]
    print(ret)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
