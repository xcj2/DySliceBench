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


def probC():
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
    minMP = 99999999999999999999
    for f in gen2Bits(N):
        dmp(f)
        mp = 0
        lg = zeros(4)
        for i in range(N):
            if lg[f[i]] > 0 and f[i] < 3:
                mp += 10
            lg[f[i]] += L[i]
            dmp((i,lg,mp))
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


