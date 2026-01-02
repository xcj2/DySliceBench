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

n, m, q = MAP()
'''
arr = [[]]
for i in range(n):
    tmp = deepcopy(arr)
    arr = []
    for j in range(1, m + 1):
        for k in range(len(tmp)):
            if len(tmp[k]) == 0 or tmp[k][-1] <= j:
                arr.append(deepcopy(tmp[k]))
                arr[-1].append(j)
'''
arr = list(combinations_with_replacement(range(1, m + 1), n))
point = [0 for _ in range(len(arr))]
for i in range(q):
    a, b, c, d = MAP()
    for j in range(len(arr)):
        if arr[j][b - 1] - arr[j][a - 1] == c:
            point[j] += d

print(max(point))
