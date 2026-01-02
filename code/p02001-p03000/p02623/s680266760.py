import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10, gcd
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
#from fractions import gcd
from decimal import *
import heapq
def debug(*args):
    if debugmode:
        print(*args)
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def FLOAT(): return float(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 1, 0, -1, 1, -1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
debugmode = True

#にぶたん
def search(arr, num):
    l = 0
    r = len(arr) - 1
    if arr[r] <= num:
        return r
    if arr[l] > num:
        return -1
    while r - l > 1:
        c = (r + l) // 2
        if arr[c] > num:
            r = c
        elif arr[c] < num:
            l = c
        else:
            r = c
            l = c
    return l

n, m, k = MAP()
a = LIST()
b = LIST()
aarr = [a[0]]
for i in range(1, n):
    aarr.append(aarr[-1] + a[i])
barr = [b[0]]
for i in range(1, m):
    barr.append(barr[-1] + b[i])

#print(aarr)
#print(barr)

ans = 0
a_n = 0
b_n = 0
tim = 0
while tim <= k:
    if a_n == -1 and b_n == -1:
        break
    elif a_n == -1:
        pls = b[b_n]
        mode = 1
    elif b_n == -1:
        pls = a[a_n]
        mode = 0
    else:
        tmp1 = k - tim + aarr[a_n - 1] if a_n != 0 else k - tim
        tmp2 = k - tim + barr[b_n - 1] if b_n != 0 else k - tim
        anum = search(aarr, tmp1) - a_n + 1
        bnum = search(barr, tmp2) - b_n + 1
        #print(tim, anum, tmp1, bnum, tmp2)
        if anum > bnum:
            pls = a[a_n]
            mode = 0
        else:
            pls = b[b_n]
            mode = 1
    #print(pls, mode)
    if tim + pls <= k:
        ans += 1
        tim += pls
        if mode == 0:
            a_n += 1
            if a_n >= n:
                a_n = -1
        else:
            b_n += 1
            if b_n >= m:
                b_n = -1
    else:
        break
print(ans)