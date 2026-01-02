import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10, gcd
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
dx = [0, 1, 0, -1, 1, -1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
debugmode = True

s = [int(i) for i in STR()]
l = len(s)
arr = [-1 for _ in range(l)]
tmp = 0
for i in range(l):
    tmp += s[i] * pow(10, l - i, 2019)
    tmp %= 2019
    arr[i] = tmp
arr.sort()
tmp = arr[0]
cnt = 1
ans = 0
for i in range(1, l):
    if tmp == arr[i]:
        cnt += 1
    else:
        ans += cnt * (cnt - 1) // 2
        if tmp == 0:
            ans += cnt
        cnt = 1
        tmp = arr[i]
ans += cnt * (cnt - 1) // 2
if tmp == 0:
    ans += cnt
print(ans)
