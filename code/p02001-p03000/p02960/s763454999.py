#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(S: str):
    ## 1の位からi+1文字のうち13で割ったもののあまりがjであるものの数
    N = len(S)
    dp = [[0]*13 for _ in range(N+1)]
    dp[0][0]=1
    list10 = range(0,10)
    list13 = range(0,13)
    keta =1
    for i in range(1,N+1):
        if S[N-i]=="?":
            for j in list10:
                addmod = j*keta%13
                for k in list13:
                    modmod = (k+addmod)%13
                    dp[i][modmod] += dp[i-1][k]%MOD
        else:
            addmod = (int(S[N-i])*keta)%13
            for k in list13:
                modmod = (k+addmod)%13
                dp[i][modmod] = dp[i-1][k]%MOD
        keta*=10
        keta%=13
    print(dp[N][5]%MOD)
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
