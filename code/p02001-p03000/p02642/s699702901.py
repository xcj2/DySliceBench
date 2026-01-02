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

n = INT()
a = LIST()
b = set(a)

NN = 10 ** 6 + 100
primes = set([])
isprime = [False for _ in range(NN + 1)]
cnt = [True for _ in range(NN + 1)]
for i in a:
    if cnt[i]:
        isprime[i] = True
        cnt[i] = False
    else:
        isprime[i] = False
for i in range(1, NN + 1):
    if not cnt[i]:
        for j in range(i * 2, NN + 1, i):
            isprime[j] = False
    if isprime[i]:
        primes.add(i)
ans = 0
for i in b:
    if isprime[i]:
        ans += 1
print(ans)
