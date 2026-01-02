#!/usr/bin/env python
# coding: utf-8

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

dp = [False for _ in range(100001)]
def main():
    x = ri()
    lp = [100, 101, 102, 103, 104, 105]
    dp[0] = True
    for p in lp:
        for i in range(x+1):
            if not dp[i]:
                continue
            if i+p > x:
                continue
            dp[i+p] = True
    if dp[x]:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
