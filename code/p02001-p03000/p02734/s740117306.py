#!/usr/bin/env python3
import sys
import copy
sys.setrecursionlimit(10**8)
INF = float("inf")

MOD = 998244353  # type: int


def array(*args, initial=0):
    pre = "["*len(args)
    post = ""
    for a in args[::-1]:
        post += " for _ in range("+str(a)+")]"
    S = pre + str(initial) + post
    return eval(S)


def solve(N: int, S: int, A: "List[int]"):
    dp = array(S+1, 3, initial=0)
    dp_past = array(S+1, 3, initial=0)
    dp[0][0] = 1
    for i in range(N):
        dp_past, dp = dp, dp_past
        # t=0軸
        for s in range(S+1):
            dp[s][:] = dp_past[s]
            # A[i]を使う
            if s == A[i]:
                dp[s][1] += i+1
                dp[s][1] %= MOD
            if s-A[i] >= 0:
                dp[s][0] += dp_past[s-A[i]][0]
                dp[s][0] %= MOD
                dp[s][1] += dp_past[s-A[i]][1]
                dp[s][1] %= MOD
                dp[s][2] += (dp[s][1]-dp_past[s][1]) * (N-i)
                dp[s][2] %= MOD

    print(dp[S][2])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S, A)


if __name__ == '__main__':
    main()
