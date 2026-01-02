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

n = INT()
a = LIST()
q = INT()
b = [0]*q
c = [0]*q
for i in range(q):
    bb, cc = MAP()
    b[i] = bb
    c[i] = cc

res = sum(a)
counter = Counter(a)
for i in range(q):
    res += counter[b[i]]*(c[i]-b[i])
    counter[c[i]] = counter[b[i]] + counter[c[i]]
    counter[b[i]] = 0
    print(res)