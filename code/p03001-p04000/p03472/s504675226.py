#!/usr/bin/env python
# coding: utf-8

import queue

def ri():
    return int(input())

def rl():
    return list(input().split())

def rli():
    return list(map(int, input().split()))

def main():
    n, h = rli()
    la = []
    lb = []
    for _ in range(n):
        a, b = rli()
        la.append(a)
        lb.append(b)
    a = max(la)
    lb = sorted([b for b in lb if b > a], reverse=True)
    ans = 0
    for b in lb:
        h -= b
        ans += 1
        if h <= 0:
            break
    if h > 0:
        ans += (h+a-1) // a
    print(ans)




if __name__ == '__main__':
    main()
