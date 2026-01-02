import sys
from math import factorial
from collections import Counter
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

N, M, Q = MAP()
req = []
for i in range(Q):
    a, b, c, d = MAP()
    req.append([a-1, b-1, c, d])

A = [[1]*N, ]
def plus(a):
    n = len(a)
    if a[n-1] !=M:
        a[n-1] = a[n-1]+1
        return a
    if n==1: return [M,]
    res = plus(a[:n-1])
    return res + [res[n-2],]

while True:
    a = A[-1]
    if a == [M]*N:
        break
    A.append(plus(a))

res = 0
for i in range(len(A)):
    temp = 0
    for j in range(Q):
        if A[i][req[j][1]] - A[i][req[j][0]] == req[j][2]:
            temp += req[j][3]
    if temp > res:
        res = temp

print(res)