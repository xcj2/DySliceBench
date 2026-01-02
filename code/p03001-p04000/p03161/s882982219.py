#!/usr/bin/env python
import sys
from collections import Counter
from itertools import permutations, combinations
from math import ceil, floor
import bisect
sys.setrecursionlimit(10 ** 6)
inf = float("inf")

def input():
    return sys.stdin.readline()[:-1]

def chmin(a, b):
    if a > b:
        return b
    else:
        return a

def chmax(a, b):
    if a < b:
        return b
    else:
        return a

def main():
    n, k = map(int, input().split())
    h = tuple(map(int, input().split()))
    dp = [inf] * 110000

    dp[0] = 0
    for i in range(n-1):
        for j in range(1, min(k+1, n-i)):
            dp[i+j] = chmin(dp[i+j], dp[i] + abs(h[i+j] - h[i]))
    print(dp[n-1])

if __name__ == '__main__':
    main()

