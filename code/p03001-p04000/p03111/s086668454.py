#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/2/24
Solved on 2019/2/24
@author: shinjisu
"""


# ABC 119
def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def zeros(n): return [0]*n


def getIntLines(n): return [int(input()) for i in range(n)]


def getIntMat(n):
    mat = []
    for i in range(n):
        mat.append(getIntList())
    return mat


def zeros2(n, m): return [zeros(m)]*n


ALPHABET = [chr(i+ord('a')) for i in range(26)]
DIGIT = [chr(i+ord('0')) for i in range(10)]
N1097 = 10**9 + 7
INF = 10**10


def dmp(x, cmt=''):
    global debug
    if debug:
        if cmt != '':
            print(cmt, ':  ', end='')
        print(x)
    return x


def gen2Bits(n):  # n個の0/1のリストを生成　[0]から変化
    bits = zeros(n)
    for i in range(4**n):
        for k in range(n):
            bits[k] = i % 4
            i //= 4
        yield bits


# 多重ループを再帰で実現
def loop(level, a, b, c, mp):
    global N, L, A, B, C, minMP
    if level == N:
        if min(a, b, c) == 0:
            return INF
        mp += abs(A-a) + abs(B-b) + abs(C-c) - 30  #  一本目にはMP不要
        dmp((minMP, mp), 'min, MP')
        minMP = min(minMP,mp)
        return minMP
    else:
        mp0 = loop(level+1, a, b, c, mp)
        mp1 = loop(level+1, a+L[level], b, c, mp+10)
        mp2 = loop(level+1, a, b+L[level], c, mp+10)
        mp3 = loop(level+1, a, b, c+L[level], mp+10)
        dmp((mp0, mp1, mp2, mp3))
        return min(mp0, mp1, mp2, mp3)


def probC():
    global N, L, A, B, C, minMP
    
    N, A, B, C = getIntList()
    L = []
    for i in range(N):
        L.append(getInt())
    dmp((N, A, B, C ))
    dmp(L)
    d = zeros(3)
    d = A, B, C
    dmp(d)
    minMP = INF
    return loop(0, 0, 0, 0, 0)


def probC_v2():
    N, A, B, C = getIntList()
    L = []
    for i in range(N):
        L.append(getInt())
    dmp((N, A, B, C ))
    dmp(L)
    d = zeros(3)
    d = A, B, C
    dmp(d)
    minMP = INF
    for f in gen2Bits(N):
        dmp(f)
        mp = 0
        lg = zeros(4)
        for i in range(N):
            if lg[f[i]] > 0 and f[i] < 3:
                mp += 10
            lg[f[i]] += L[i]
            #dmp((i,lg,mp))
        #dmp(lg)
        if min(lg[:3]) == 0:  # 4番目は使用しない竹
            continue
        for i in range(3):
            mp += abs(lg[i]-d[i])
        dmp((minMP, mp), 'min, MP')
        minMP = min(minMP, mp)
    return minMP


def probC_v1():
    N, A, B, C = getIntList()
    L = []
    for i in range(N):
        L.append(getInt())
    dmp((N, A, B, C ))
    dmp(L)
    d = zeros(3)
    d[0] = A
    d[1] = B
    d[2] = C
    dmp(d)
    minMP = INF
    for f in gen2Bits(N):
        dmp(f)
        mp = 0
        lg = zeros(4)
        for i in range(N):
            if lg[f[i]] > 0 and f[i] < 3:
                mp += 10
            lg[f[i]] += L[i]
            #dmp((i,lg,mp))
        #dmp(lg)
        allUsed = True
        for i in range(3):  # 4番目は使用しない竹
            if lg[i] == 0:
                allUsed = False
                break
            mp += abs(lg[i]-d[i])
        if not allUsed:
            continue
        dmp((minMP, mp))
        minMP = min(minMP, mp)
    return minMP


debug = False  # True False
print(probC())


def gcd(x, y):  # 最大公約数
    m = max(x, y)
    n = min(x, y)
    while m % n != 0:
        w = m % n
        m = n
        n = w
    return n


def probD():
    N, M = getIntList()
    A = getIntList()
    dmp((N, M))
    dmp(A)
    return num


def probA():
    S = input()
    dmp(S)
    y = int(S[0:4])
    m = int(S[5:7])
    d = int(S[8:10])
    dmp((y,m,d))
    HEI = 'Heisei'
    if y <= 2018:
        return HEI
    if m <= 4:
        return HEI
    else:
        return 'TBD'


def probB():
    N = getInt()
    dmp(N)
    sm = 0.0
    for i in range(N):
        x, u = [a for a in input().split()]
        dmp((x,u))
        if u == 'JPY':
            x = int(x)
        else:
            x = float(x) * 380000.0
        sm += x
    return sm


