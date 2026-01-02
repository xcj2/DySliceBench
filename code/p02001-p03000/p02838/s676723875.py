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
    targets = LI()

    ttl_bins = [0]*60
    for i in range(N):
        target = targets[i]
        target_str = format(target, f"0{60}b")
        for keta in range(60):
            ttl_bins[keta] += int(target_str[keta])

    ans = 0
    for i in range(60):
        ttl = ttl_bins[i] * (N - ttl_bins[i])
        ans += pow(2, 59-i, MOD) * ttl
        ans %= MOD

    print(ans)


main()
