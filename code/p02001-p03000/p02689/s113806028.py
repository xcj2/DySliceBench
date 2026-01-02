import sys
from math import factorial
from collections import Counter
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

n, m = MAP()
H = LIST()
low = []
for i in range(m):
    a, b= MAP()
    if H[a-1] == H[b-1]:
        low.append(a-1)
        low.append(b-1)
    elif H[a-1] < H[b-1]:
        low.append(a-1)
    else:
        low.append(b-1)

print(n-len(set(low)))