#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 20:41:09 2019

@author: shinjisu
"""


# 2019/2/9 Yahoo
def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def getIntLines(n): return [int(input()) for i in range(n)]


def zeros(n): return [0]*n


def db(x):
    global debug
    if debug:
        print(x)


def probA():
    N, K = getIntList()
    db((N, K))
    if (N+1)//2>=K:
        return 'YES'
    else:
        return 'NO'


def probB():
    a, b = zeros(3), zeros(3)
    db((a,b))
    for i in range(3):
        a[i], b[i] = getIntList()
    db((a,b))
    c = set([])
    e = zeros(5)
    for i in range(3):
        c.add(a[i])
        c.add(b[i])
        e[a[i]] += 1
        e[b[i]] += 1
    db((c,e))
    c0,c1,c2,c3,c4=0,0,0,0,0
    for i in range(1, 5):
        if e[i]==0:
            c0 += 1
        elif e[i] == 1:
            c1 += 1
        elif e[i] == 2:
            c2 += 1
        elif e[i] == 3:
            c3 += 1
        else:
            c4 += 1
    db((c0,c1,c2,c3,c4))
    if c1 == 2 and c2 == 2: 
        return 'YES'
    else:
        return 'NO'


def probC():
    K, A, B = getIntList()
    db((K,A,B))
    if B-A < 3:
        bCount = 1 + K
    elif 1+K < A:
        bCount = 1 + K
    else:
        remK = 1+K-A  # ビスケットはA枚
        db(remK)
        bCount = A
        bCount += remK//2*(B-A)
        bCount += remK % 2
    return bCount


def issuedCode():
    for i in range(1, 10**9):
        if (1+K-i*2)//A==i:
            break
        db(i)
    bCount = B*i + (K-2*i)


debug = False
print(probC())
