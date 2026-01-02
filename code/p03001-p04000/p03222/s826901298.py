#!/usr/bin/env python3

from copy import deepcopy
MOD = 10 ** 9 + 7

def main():
    h, w, k = map(int, input().split())
    ways = []
    for way in range(2 ** (w - 1)):
        if isvalid(way):
            ways.append(way)
    dp = [0 for i in range(w)]
    dp[0] = 1
    for i in range(h):
        dppre = deepcopy(dp)
        dp = [0 for i in range(w)]
        for j in range(w):
            for way in ways:
                dp[j] += dppre[apply(way, j)]
                dp[j] %= MOD
    print(dp[k - 1])

def apply(way, fr):
    logic = [False]
    for d in range(8):
        logic.append(bool(way & 1))
        way >>= 1
    if logic[fr]:
        to = fr - 1
    elif logic[fr + 1]:
        to = fr + 1
    else:
        to = fr
    return to

def isvalid(way):
    logic = []
    for d in range(7):
        logic.append(bool(way & 1))
        way >>= 1
    for d in range(6):
        if logic[d] & logic[d + 1]:
            return False
    return True

if __name__ == "__main__":
    main()
