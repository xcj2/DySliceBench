import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
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
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
debugmode = False

a = LIST()
ans = 0
a.sort()
m = a[-1]
d = 0
if 3 * m % 2 == sum(a) % 2:
    d = m
else:
    d = m + 1
ans = 0
while not a[0] == a[1] == a[2]:
    if a[0] < d and a[1] < d:
        ans += 1
        a[0] += 1
        a[1] += 1
    elif a[0] < m:
        ans += 1
        a[0] += 2
    else:
        ans += 1
        a[1] += 2
    if a[0] > d or a[1] > d:
        break
    debug(a)
print(ans)