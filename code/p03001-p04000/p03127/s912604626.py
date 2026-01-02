#!/usr/bin/env python
# -*- coding: utf-8 -*-

def gcd(a, b):
    if a < b:
        a,b = b,a
    while b > 0:
        r = a % b
        a,b = b,r
    return a

def arrgcd(a):
    alen = len(a)
    if alen == 3:
        return gcd(a[0], gcd(a[1], a[2]))
    elif alen == 2:
        return gcd(a[0], a[1])
    elif alen == 1:
        return a[0] # 最初から1つ
    elif alen == 0:
        return 0
    else:
        return gcd(arrgcd(a[:alen//2]), arrgcd(a[alen//2:]))

def solve():
    n = int(input())
    al = [int(i) for i in input().split()]
    print(arrgcd(al))

if __name__=="__main__":
    solve()
