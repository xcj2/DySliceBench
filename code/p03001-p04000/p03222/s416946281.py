#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

p = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def count(n):
    if n <= 0:
        return 1
    return p[n]

MOD = 1000000007

def main():
    H, W, K = rli()
    dp = [[0 for _ in range(W+2)] for _ in range(H+1)]
    dp[0][1] = 1
    for h in range(0, H):
        for w in range(1, W+1):
            dp[h+1][w] = dp[h][w-1]*count(w-3)*count(W-w-1)
            dp[h+1][w] += dp[h][w]*count(w-2)*count(W-w-1)
            dp[h+1][w] += dp[h][w+1]*count(w-2)*count(W-w-2)
            dp[h+1][w] %= MOD
    print(dp[H][K])


if __name__ == '__main__':
    main()
