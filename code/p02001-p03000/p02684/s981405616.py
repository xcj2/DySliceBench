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

n, k = MAP()
a = LIST()
arr = set([])
loop = []
i = 0
idx = 0
cnt = -1
flag = True
flag2 = True
strt = -1
while i < k:
    idx = a[idx] - 1
    i += 1
    l = len(arr)
    arr.add(idx)
    if l == len(arr) and flag:
        flag = False
        cnt = 1
        strt = idx
        loop.append(idx)
    elif not flag and idx == strt:
        flag2 = False
        break
    elif not flag:
        cnt += 1
        loop.append(idx)
    #debug(idx, loop)
#debug(arr, loop, cnt, flag, flag2)
if flag2:
    print(idx + 1)
else:
    print(loop[(k - i) % cnt] + 1)