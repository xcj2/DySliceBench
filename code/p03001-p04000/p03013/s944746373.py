#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32

MOD = 1000000007  # type: int

def solve(N: int, M: int, a: "List[int]"):
    dp = [-1] *(N+2)
    ckc = [True] * (N+2)
    for i in a:
        ckc[i] = False

    def f(n: int):
        if(dp[n] != -1):
            return dp[n]

        if n <= 0:
            dp[n] = 0
        else:
            if not ckc[n-1] and not ckc[n-2]:
                dp[n] = 0
            elif not ckc[n-1]:
                dp[n] = f(n-2) % MOD
            elif not ckc[n-2]:
                dp[n] = f(n-1) % MOD
            else:
                dp[n] = (f(n-1) + f(n-2)) % MOD
            
        return dp[n]

    dp[0] = 1
    f(N)
    print(dp[N])
    # print(dp)

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
