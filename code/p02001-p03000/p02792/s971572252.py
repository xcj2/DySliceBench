#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    dp = [[0 for _ in range(10)] for _ in range(10)]
    ans = 0
    for i in range(1, n+1):
        s = str(i)
        l = int(s[0])
        r = int(s[-1])
        dp[l][r] += 1
    for i in range(1, n+1):
        s = str(i)
        l = int(s[0])
        r = int(s[-1])
        # print(i, l, r, dp[l][r], dp[r][l])
        ans += dp[r][l]
    print(ans)


if __name__ == '__main__':
    main()
