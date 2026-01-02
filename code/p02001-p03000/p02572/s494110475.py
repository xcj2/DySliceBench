#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


MOD = 10 ** 9 + 7


def main():
    N = II()
    target = LI()

    ans = 0
    sums = [0] * N
    sum_all = target[0]
    sums[0] = target[0]
    for i in range(1, N):
        sum_all += target[i] % MOD
        sums[i] = sums[i-1] + target[i]

    for i in range(N):
        ans += target[i] * (sum_all - sums[i])
        ans = ans % MOD

    print(ans)


main()
