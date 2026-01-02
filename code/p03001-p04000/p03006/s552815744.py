#!/usr/bin/env python
# coding: utf-8

from collections import Counter

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n = ri()
    lx, ly = [], []
    for _ in range(n):
        x, y = rli()
        lx.append(x)
        ly.append(y)
    dd = {}
    dc = Counter()
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            d = (lx[i]-lx[j], ly[i]-ly[j])
            dd[(i, j)] = d
            dc[d] += 1
    if len(dc) == 0:
        print(n)
    else:
        v = dc.most_common()[0][1]
        print(n-v)


if __name__ == '__main__':
    main()
