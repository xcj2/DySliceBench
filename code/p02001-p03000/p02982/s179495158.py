#!/usr/bin/env python
# coding: utf-8

import math

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def dist(a, b):
    d = 0
    for a1, b1 in zip(a, b):
        d += (a1-b1)**2
    d = math.sqrt(d)
    return (d-int(d)) < 0.00001

def main():
    n, d = rli()
    lp = []
    for _ in range(n):
        lx = rli()
        lp.append(lx)
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if dist(lp[i], lp[j]):
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
