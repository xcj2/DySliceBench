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

n, k = MAP()
a = LIST()
tugi = [0]+a
town  =1
route = [0]*n
route[0] = town
used = [False]*n
used[0] = True
for i in range(n):
    town = tugi[town]
    if used[town-1]:
        i = route.index(town)
        notcycle = route[:i]
        cycle = route[i:]
        break
    used[town-1] = True
    route[i+1] = town

for i in range(n):
    if cycle[i] == 0:
        cycle = cycle[:i]
        break

if len(notcycle) >k:
    print(notcycle[k])
else:
    k -= len(notcycle)
    print(cycle[k%len(cycle)])