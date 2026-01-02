import sys
from collections import Counter, deque, defaultdict, OrderedDict
from math import factorial
from fractions import Fraction
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))


MOD = 998244353
n = INT()
d = LIST()
if d[0] != 0:
    print(0)
    sys.exit()
d = d[1:]
c = dict(Counter(d))
c =  OrderedDict(sorted(c.items()))
c = list(c.values())
if len(c) != max(d):
    print(0)
    sys.exit()
res = 1
for i in range(1, len(c)):
    res *= c[i-1]**c[i]

print(res%MOD)