#!/usr/bin/env python3

import sys
sys.setrecursionlimit(300000)


def solve(N: int, K: int, C: int, S: str):
    memo = [-1] * (N + 1)
    def rec(idx):
        if idx >= N:
            idx = N
            memo[idx] = 0
            return memo[idx]
        if memo[idx] >= 0:
            return memo[idx]
        if S[idx] == 'o':
            ret = 1 + rec(idx + C + 1)
        else:
            ret = rec(idx + 1)
        memo[idx] = ret
        return ret

    dp = [0] * (N + 1)
    for i in range(N):
        if memo[i] < 0:
            rec(i)
        dp[i + 1] = max(dp[i + 1], dp[i])
        if S[i] == 'o':
            if i - C < 0:
                tmp = 0
            else:
                tmp = dp[i - C]
            dp[i + 1] = max(dp[i + 1], tmp + 1)
    #print(memo)
    #print(dp)

    ret = []
    for i in range(N):
        if S[i] == 'o' and dp[i] + memo[i + 1] < K:
            ret.append(i + 1)
    if not ret:
        print('')
    for r in ret:
        print(r)
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, K, C, S)

if __name__ == '__main__':
    main()
