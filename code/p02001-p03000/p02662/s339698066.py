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
mod = 998244353
dx = [0, 1, 0, -1, 1, -1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
debugmode = True

n2 = [1 for _ in range(3010)]
for i in range(1, 3010):
    n2[i] = n2[i - 1] * 2 % mod

n, s = MAP()
a = LIST()
dp = [[0 for _ in range(s + 1)] for _ in range(n)]
if s >= a[0]:
    dp[0][a[0]] = 1
for i in range(1, n):
    for j in range(1, min(s + 1, a[i])):
        dp[i][j] = dp[i - 1][j] * 2
        dp[i][j] %= mod
    if a[i] <= s:
        dp[i][a[i]] = dp[i - 1][a[i]] * 2 + n2[i]
        dp[i][a[i]] %= mod
    for j in range(a[i] + 1, s + 1):
        dp[i][j] = dp[i - 1][j] * 2 + dp[i - 1][j - a[i]]
        dp[i][j] %= mod
print(dp[n - 1][s])
