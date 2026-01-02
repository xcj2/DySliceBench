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
    N, W = map(int, input().split())
    w = [0]
    v = [0]
    for i in range(N):
        a, b = map(int, input().split())
        w.append(a)
        v.append(b)

    dp = []
    for i in range(N + 1):
        dp.append([0] * (W + 1))

    for i in range(1, N + 1):
        for j in range(1, W + 1):
            dp[i][j] = dp[i - 1][j]
            if j - w[i] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
    print(dp[N][W])

if __name__ == '__main__':
    main()
