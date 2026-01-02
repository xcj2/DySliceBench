#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 05:38:56 2019

@author: shinjisu
"""


# ABC 200点問題
import math


def getInt(): return int(input())


def getIntList(): return [int(x) for x in input().split()]


def zeros(n): return [0]*n


def dmp(x):
    global debug
    if debug:
        print(x)


debug = True


def getIntLines(n): return [int(input()) for i in range(n)]


def getIntMat(n):
    mat = []
    for i in range(n):
        mat.append(getIntList())
    return mat


def zeros2(n, m): return [zeros(m)]*n


def prob096():  # Maximum Sum
    X = getIntList()
    K = getInt()
    dmp((X, K))
    total = sum(X) - max(X) + max(X)*2**K
    return total


def prob097():  # Exponential
    X = getInt()
    dmp(X)
    if X == 1:
        return 1
    for n in range(X, 0, -1):
        dmp(n)
        for b in range(2, int(math.sqrt(X))+1):
            a = n
            exp = True
            while a > 1:
                if a % b != 0:
                    exp = False
                    break
                a //= b
            if exp:
                break
        if exp:
            break
    return n


def prob098():  # Cut and Count
    N = getInt()
    S = input()
    dmp((N, S))
    maxChCount = 0
    for i in range(1, N):
        before = S[:i]
        after = S[i:]
        dmp((before, after))
        chCount = 0
        for j in range(26):
            ch = chr(ord('a')+j)
            if ch in before and ch in after:
                chCount += 1
        maxChCount = max(maxChCount, chCount)
    return maxChCount


def prob099():  # Stone Momument
    a, b = getIntList()
    height = 0
    for i in range(b-a+1):
        height += i
    height -= b
    return height


def prob103():  # String Rotation
    S = input()
    T = input()
    for i in range(len(S)):
        S = S[1:] + S[0]
        dmp(S)
        if S == T:
            return 'Yes'
    else:
        return 'No'


def prob110():  # 1 Dimensional World's Tale
    N, M, X, Y = getIntList()
    cX = getIntList()
    cY = getIntList()
    dmp((N, M, X, Y))
    dmp(cX)
    dmp(cY)
    NW = 'No War'
    WA = 'War'
    if Y <= X:
        return WA
    cX.sort()
    cY.sort()
    dmp(cX)
    dmp(cY)
    if cX[-1] < cY[0] and \
            X < cY[0] and \
            cX[-1] < Y:
        return NW
    else:
        return WA


def prob109():  # Shiritori
    N = getInt()
    W = []
    for i in range(N):
        W.append(input())
    dmp(W)
    ALPHABET = [chr(i+ord('a')) for i in range(26)]
    NO = 'No'
    dmp(ALPHABET)
    used = set([W[0]])
    for i in range(1, N):
        dmp(used)
        if W[i] in used:
            return NO
        used.add(W[i])
        if W[i-1][-1] != W[i][0]:
            return NO
    return 'Yes'


def prob106():  # 105
    N = getInt()
    div8Count = 0
    for i in range(1, N+1):
        divCount = 0
        for j in range(1, i+1):
            #dmp(('i,j',i,j))
            if i % j == 0:
                divCount += 1
        dmp((i,divCount))
        if divCount == 8 and i % 2 == 1:
            div8Count += 1
    return div8Count


def prob107():  # Grid Compression
    H, W = getIntList()
    grid = []
    for i in range(H):
        grid.append(input())
    dmp((H,W))
    dmp(grid)
    WHITE = '.'
    i = 0
    while i < len(grid):
        for cell in grid[i]:
            if cell != WHITE:
                i += 1
                break
        else:
            grid.pop(i)
    dmp(grid)
    j = 0
    while j < len(grid[0]):
        for i in range(len(grid)):
            if grid[i][j] != WHITE:
                j += 1
                break
        else:
            for i in range(len(grid)):
                grid[i] = grid[i][:j] + grid[i][j+1:]
    return grid


def prob100():  # 
    return 0


debug = False  # True False
#print(prob107())
w = prob107()
for row in w:
    print(row)