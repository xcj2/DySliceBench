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

isprime = {a[i]:True for i in range(n)}

for i in range(n): 
    if not isprime[a[i]]: continue
    j = 2
    while a[i]*j < a[-1]+1:
        if isprime.get(a[i]*j) == True:
            isprime[a[i]*j] = False
        j += 1

ensem = list(c.values())
key = list(c.keys())
diff = len([i for i in range(len(c)) if ensem[i] != 1 and isprime[key[i]]])
print(list(isprime.values()).count(True)-diff)