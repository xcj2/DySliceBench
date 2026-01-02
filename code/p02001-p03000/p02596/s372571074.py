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

k = INT()
l = len(str(k))
if k % 2 == 0:
    print(-1)
    exit()
dp = [-1 for _ in range(10 ** 6 + 100)]
for i in range(10 ** 6 + 100):
    if l > i + 1:
        continue
    elif l == i + 1:
        num = 0
        for _ in range(i):
            num *= 10
            num += 7
        if k > num:
            continue
    if dp[i - 1] == -1:
        num = 0
        for _ in range(i):
            num *= 10
            num += 7
        dp[i] = num % k
    else:
        dp[i] = (dp[i - 1] * 10 + 7) % k
    if dp[i] == 0:
        print(i)
        exit()
print(-1)