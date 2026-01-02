#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2019/2/24
Solved on 2019/2/24-25
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


# def zeros2(n, m): return [zeros(m)]*n
def zeros2(n, m):
    d2 = zeros(n)
    for i in range(n):
        d2[i] = zeros(m)
    return d2


ALPHABET = [chr(i+ord('a')) for i in range(26)]
DIGIT = [chr(i+ord('0')) for i in range(10)]
N1097 = 10**9 + 7
INF = 10**12


def dmp(x, cmt=''):
    global debug
    if debug:
        if cmt != '':
            print(cmt, ':  ', end='')
        print(x)
    return x


# valをlstにあるか lstは昇順にソートされている必要がある
# 一致する場合は添え字を返す しない場合は区間を構成する要素の大きい方の添え字
# [0]より小さい場合は0、[n-1]より大きい場合はnを通知する
def lookup_v1(val, lst):
    #dmp((val, lst),'lookup')
    for i in range(len(lst)):
        if val <= lst[i]:
            return i
    else:
        return len(lst)


def solve_v1(pos):
    global S, T
    dmp(pos,'pos')
    minD = INF
    # 神社->寺
    i1 = lookup(pos, S)
    i2 = lookup(S[i1-1], T)
    d1 = abs(T[i2-1]-S[i1-1]) + abs(S[i1-1]-pos)
    d2 = abs(T[i2]-S[i1-1]) + abs(S[i1-1]-pos)
    minD = min(minD, d1, d2)
    dmp(minD,'minD')
    i2 = lookup(S[i1], T)
    d1 = abs(T[i2-1]-S[i1]) + abs(S[i1]-pos)
    d2 = abs(T[i2]-S[i1]) + abs(S[i1]-pos)
    minD = min(minD, d1, d2)
    dmp(minD,'minD')
    # 寺->神社
    i1 = lookup(pos, T)
    i2 = lookup(T[i1-1], S)
    d1 = abs(S[i2-1]-T[i1-1]) + abs(T[i1-1]-pos)
    d2 = abs(S[i2]-T[i1-1]) + abs(T[i1-1]-pos)
    minD = min(minD, d1, d2)
    dmp(minD,'minD')
    i2 = lookup(T[i1], S)
    d1 = abs(S[i2-1]-T[i1]) + abs(T[i1]-pos)
    d2 = abs(S[i2]-T[i1]) + abs(T[i1]-pos) 
    minD = min(minD, d1, d2)
    dmp(minD,'minD')
    return minD


# v2
def getMinDist_v2(level, pos, ST, TS):
    dmp((level,pos),'level,pos')
    if level == 2:
        return INF
    minD = INF
    # 神社->寺
    is1, is2 = lookup(pos, ST)
    it1, it2 = lookup(ST[is1], TS)
    d1 = abs(TS[it1]-ST[is1]) + abs(ST[is1]-pos)
    d2 = abs(TS[it2]-ST[is1]) + abs(ST[is1]-pos)
    minD = min(minD, d1, d2)
    dmp(minD,'minD')
    if is1 != is2:
        dmp(is2, 'is2')
        it1, it2 = lookup(ST[is2], TS)
        d1 = abs(TS[it1]-ST[is2]) + abs(ST[is2]-pos)
        d2 = abs(TS[it2]-ST[is2]) + abs(ST[is2]-pos)
        minD = min(minD, d1, d2)
        dmp(minD,'minD')
    return min(minD, getMinDist(level+1, pos, TS, ST))


def solve_v2(pos):
    global S, T
    return getMinDist(0, pos, S, T)


# バイナリサーチ 区間を返す
def lookup(val, lst):
    dmp((val, lst), 'lookup')
    left = 0
    right = len(lst) - 1
    if val < lst[0]:
        return 0, 0
    elif val > lst[-1]:
        return len(lst)-1, len(lst)-1
    while left+1 < right:
        mid = (left+right) // 2
        if val <= lst[mid]:
            right = mid
        else:
            left = mid
    dmp((left, right))
    return left, right


def getMinDist(level, pos, ST, TS):
    dmp((level,pos),'level,pos')
    if level == 2:
        return INF
    minD = INF
    # 神社->寺
    d1 = abs(TS[it1]-ST[is1]) + abs(ST[is1]-pos)
    d2 = abs(TS[it2]-ST[is1]) + abs(ST[is1]-pos)
    minD = min(minD, d1, d2)
    dmp(minD,'minD')
    if is1 != is2:
        dmp(is2, 'is2')
        d1 = abs(TS[it1]-ST[is2]) + abs(ST[is2]-pos)
        d2 = abs(TS[it2]-ST[is2]) + abs(ST[is2]-pos)
        minD = min(minD, d1, d2)
        dmp(minD,'minD')
    return min(minD, getMinDist(level+1, pos, TS, ST))


def solve(pos):
    is1, is2 = lookup(pos, S)
    it1, it2 = lookup(pos, T)
    minD = INF
    d1 = abs(T[it1]-S[is1]) + abs(S[is1]-pos)
    d2 = abs(T[it2]-S[is1]) + abs(S[is1]-pos)
    d3 = abs(T[it1]-S[is2]) + abs(S[is2]-pos)
    d4 = abs(T[it2]-S[is2]) + abs(S[is2]-pos)
    d5 = abs(S[is1]-T[it1]) + abs(T[it1]-pos)
    d6 = abs(S[is2]-T[it1]) + abs(T[it1]-pos)
    d7 = abs(S[is1]-T[it2]) + abs(T[it2]-pos)
    d8 = abs(S[is2]-T[it2]) + abs(T[it2]-pos)
    minD = min(minD, d1, d2, d3, d4, d5, d6, d7, d8)

    dmp(minD)
    return minD


def probD():
    global S, T
    A, B, Q = getIntList()
    S = getIntLines(A)
    T = getIntLines(B)
    X = getIntLines(Q)
    dmp((A, B, Q), 'A, B, Q')
    dmp(S,'S')
    dmp(T,'T')
    dmp(X,'X')
    S = [-INF] + S + [INF]
    T = [-INF] + T + [INF]
    for x in X:
        print(solve(x))
    return ''


debug = False  # True False
print(probD())


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


# 多重ループを再帰で実現
def loop(level, a, b, c, mp):
    global N, L, A, B, C, minMP
    if level == N:
        if min(a, b, c) == 0:
            return INF
        mp += abs(A-a) + abs(B-b) + abs(C-c) - 30  # 一本目にはMP不要
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


# 96msec
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


def gen2Bits(n):  # n個の0/1/2/3のリストを生成　[0]から変化
    bits = zeros(n)
    for i in range(4**n):
        for k in range(n):
            bits[k] = i % 4
            i //= 4
        yield bits


# 436msec
def probC_v2():
    N, A, B, C = getIntList()
    L = []
    for i in range(N):
        L.append(getInt())
    dmp((N, A, B, C))
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
    dmp((N, A, B, C))
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
