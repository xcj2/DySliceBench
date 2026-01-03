#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def identity(x):
    return x

def mapv(f,s):
    return list(map(f,s))

def readln():
    _res = mapv(int,str(input()).split(' '))
    return _res

def seq(n,f=(lambda x: 0)):
    return [f(i) for i in range(0,n)]

n,c,k = readln()
t = [0 for i in range(0,n)]
for i in range(0,n):
    t[i] = int(input())
t = sorted(t)
ans,left = 0,0
while left < n:
    right = left
    while right < n and right - left < c and t[right] - t[left] <= k :
        right = right + 1
    ans = ans + 1
    left = right
print(ans)
