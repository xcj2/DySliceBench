#!/usr/bin/env python3
import sys
import math
import decimal
import itertools
from itertools import product
from functools import reduce
def input():
    return sys.stdin.readline()[:-1]
def gcd(*numbers):
    return reduce(math.gcd, numbers)
def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def sort_zip(a:list, b:list):
    z = zip(a, b)
    z = sorted(z)
    a, b = zip(*z)
    a = list(a)
    b = list(b)
    return a, b
def ceil(x):
    return math.ceil(x)
def floor(x):
    return math.floor(x)


def main():
    MOD = 998244353
    N, K = map(int, input().split())
    L = [0] * K
    R = [0] * K
    for i in range(K):
        L[i], R[i] = map(int, input().split())

    dp = [0] * (N + 1)
    dpsum = [0] * (N + 1)
    dp[1] = 1
    dpsum[1] = 1
    for i in range(2, N + 1):
        for j in range(K):
            li = i - R[j]
            li = max(li, 1)
            ri = i - L[j]
            if ri < 0:
                continue
            dp[i] += (dpsum[ri] - dpsum[li - 1]) % MOD
        dpsum[i] += (dpsum[i - 1] + dp[i]) % MOD
    print(dp[N] % MOD)


if __name__ == '__main__':
    main()
