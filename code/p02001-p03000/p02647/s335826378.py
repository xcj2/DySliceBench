import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10, gcd
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
#from fractions import gcd
from decimal import *
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

n, k = MAP()
a = LIST()
for j in range(k):
    prea = [i for i in a]
    num = [0 for _ in range(n + 2)]
    for i in range(n):
        l = max(1, i + 1 - a[i])
        r = min(n + 1, i + 1 + a[i] + 1)
        num[l] += 1
        num[r] -= 1
    for i in range(1, n + 2):
        num[i] += num[i - 1]
    #print(num)
    a = [i for i in num[1:n + 1]]
    if a == prea:
        break
a = [str(i) for i in a]
print(' '.join(a))