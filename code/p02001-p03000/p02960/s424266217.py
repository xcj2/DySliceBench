#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(S: str):
    N = len(S)
    dp = [[0 for _ in range(13)] for _ in range(len(S))]
    if S[N-1] != '?':
        dp[0][int(S[N-1])] = 1
    else:
        dp[0] = [1,1,1,1,1,1,1,1,1,1,0,0,0]
    ten = [1]
    for i in range(1, len(S)):
        ten.append(ten[-1] * 10 % 13)
        ii = len(S) - i - 1
        for j in range(13):
            if S[ii] == '?':
                for ll in range(10):
                    kk = ll * ten[i] % 13
                    dp[i][j] += dp[i-1][(13 + j - kk)%13]
                    dp[i][j] %= MOD
            else:
                x = int(S[ii])
                m = x * ten[i] % 13
                dp[i][j] = dp[i-1][(13+j-m)%13]
                dp[i][j] %= MOD
    print(dp[len(S)-1][5])
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
