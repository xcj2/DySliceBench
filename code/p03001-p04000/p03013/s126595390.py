#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def solve(N: int, M: int, a: "List[int]"):
    dp = [0] * (N + 1)
    dp[0] = 1
    j = 0
    for i in range(N):
        if j < M and i == a[j]:
            dp[i] = 0
            j += 1
        if i + 1 <= N:
            dp[i + 1] += dp[i]
        if i + 2 <= N:
            #print(i + 2)
            dp[i + 2] += dp[i]
    ret = dp[N] % MOD
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
    a = [ int(next(tokens)) for _ in range(M) ]  # type: "List[int]"
    solve(N, M, a)

if __name__ == '__main__':
    main()
