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

def Base_10_to_n(X, n):
    X_dumy = X
    out = []
    while X_dumy>0:
        n_out = [X_dumy%n]
        n_out.extend(out)
        out = deepcopy(n_out)
        X_dumy = int(X_dumy/n)
    return out

n = INT()
m = Base_10_to_n(n, 26)
#print(m)
m = [i - 1 for i in m]
#print(m)
for i in reversed(range(1, len(m))):
    if m[i] < 0:
        m[i] += 26
        m[i - 1] -= 1
#print(m)
strt = 0
for i in range(len(m)):
    if m[i] < 0:
        strt = i + 1
    else:
        break
ans = ''
for i in m[strt:]:
    ans += chr(ord('a') + i)
print(ans)
