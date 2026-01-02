#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


MOD = 998244353


def main():
    N, K = MI()

    kukan = []
    for _ in range(K):
        tmp = LI()
        kukan.append(tmp)

    dp = [0] * (N + 1)
    dp[1] = 1
    dp_sum = [0] * (N+1)
    dp_sum[1] = 1

    for i in range(N+1):
        for k in range(K):
            l, r = kukan[k]
            pre_l = i - r
            pre_r = i - l
            if pre_r < 0:
                continue
            pre_l = max(pre_l, 0)
            dp[i] += dp_sum[pre_r] - dp_sum[pre_l - 1]

        dp_sum[i] = dp[i] + dp_sum[i-1]
        dp_sum[i] %= MOD
        dp[i] %= MOD

    print(dp[-1])


main()
