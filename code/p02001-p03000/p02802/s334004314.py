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
    n, m = rli()
    wa = [0 for _ in range(n)]
    ac = [0 for _ in range(n)]
    for i in range(m):
        p, s = rl()
        p = int(p)
        p -= 1
        if ac[p] > 0:
            continue
        if s == "WA":
            wa[p] += 1
        else:
            ac[p] = 1
    sac = sum(ac)
    swa = sum(wa[i] for i in range(len(wa)) if ac[i] > 0)
    print(sac, swa)


if __name__ == '__main__':
    main()
