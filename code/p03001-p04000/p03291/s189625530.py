#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(S: str):
    total = 0
    for s in S:
        if s == '?':
            total += 1
    tri = [1]
    for i in range(1, total + 1):
        tri.append(tri[i - 1] * 3 % MOD)
    n = len(S)
    dp = [[0] * 4 for _ in range(n + 1)]
    cnt = 0
    for i in range(n):
        s = S[i]
        #dp[i + 1][0] = dp[i][0]
        #dp[i + 1][1] = dp[i][1]
        #dp[i + 1][2] = dp[i][2]
        #dp[i + 1][3] = dp[i][3]
        if s == '?':
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1] + 1
            dp[i + 1][2] = (dp[i][2] * 3 + dp[i][0] * tri[cnt] + dp[i][1] * tri[cnt - 1]) % MOD
            dp[i + 1][3] = (dp[i][3] + dp[i][2] * tri[total - cnt - 1]) % MOD
            cnt += 1
        elif s == 'A':
            dp[i + 1][0] = dp[i][0] + 1
            dp[i + 1][1] = dp[i][1]
            dp[i + 1][2] = dp[i][2]
            dp[i + 1][3] = dp[i][3]
        elif s == 'B':
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1]
            dp[i + 1][2] = (dp[i][2] + dp[i][0] * tri[cnt] + dp[i][1] * tri[cnt - 1]) % MOD
            dp[i + 1][3] = dp[i][3]
        elif s == 'C':
            dp[i + 1][0] = dp[i][0]
            dp[i + 1][1] = dp[i][1]
            dp[i + 1][2] = dp[i][2]
            dp[i + 1][3] = (dp[i][3] + dp[i][2] * tri[total - cnt]) % MOD
    #print(dp)
    ret = dp[n][3] % MOD
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
