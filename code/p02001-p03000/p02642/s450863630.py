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
c = Counter(a)
a = sorted(a)
M = max(a)
isprime = [0]*(M+1)

for i in range(n):
    if isprime[a[i]]==0:
        isprime[a[i]] = 1
        tmp = 2
        while a[i]*tmp < M+1:
            isprime[a[i]*tmp] = 2
            tmp += 1
    elif isprime[a[i]] == 1:
        isprime[a[i]] = 2

ans = 0
for ele in a:
    if isprime[ele] != 2:
        ans += 1
print(ans)