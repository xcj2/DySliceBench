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
    N = int(input())
    h = list(map(int, input().split()))

    INF = 10**18
    dp = [INF] * N

    dp[0] = 0
    dp[1] = abs(h[1] - h[0])

    for i in range(2, N):
        a = dp[i - 1] + abs(h[i] - h[i - 1])
        b = dp[i - 2] + abs(h[i] - h[i - 2])
        dp[i] = min(a, b)

    print(dp[-1])


if __name__ == '__main__':
    main()
