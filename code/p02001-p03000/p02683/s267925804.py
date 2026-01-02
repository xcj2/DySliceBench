import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10, gcd
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
#from fractions import gcd
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

n, m, x = MAP()
arr = [LIST() for _ in range(n)]
c = [arr[i][0] for i in range(n)]
a = [arr[i][1:] for i in range(n)]

ans = inf
for i in range(2 ** n):
    tmp = [0 for _ in range(m)]
    cst = 0
    for j in range(n):
        if i - (i >> (j + 1)) * (2 ** (j + 1)) >= 2 ** j:
            for k in range(m):
                tmp[k] += a[j][k]
            cst += c[j]
    flag = True
    for j in range(m):
        if tmp[j] < x:
            flag = False
    if flag:
        ans = min(ans, cst)
if ans == inf:
    print(-1)
else:
    print(ans)