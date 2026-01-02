#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(N: int, M: int, a: "List[int]"):
    #dp[i] = i段目までの移動総数
    dp = [-1]*(N+1)
    dp[0]=1
    dp[1]=1 
    for i in range(M):
        dp[a[i]] = 0
    
    for i in range(2,N+1):
        if dp[i] == 0:
            continue
        dp[i] = dp[i-1]+dp[i-2]
        dp[i]%=MOD
    print(dp[N]%MOD)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()
