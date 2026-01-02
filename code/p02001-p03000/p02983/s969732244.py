from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial
from bisect import bisect_left, bisect_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce
#from fractions import gcd
#from math import gcd
import sys
def I(): return int(input())
def Is(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def IR(n): return [I() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def TIR(n): return [TI() for _ in range(n)]
def S(): return input()
def Ss(): return input().split()
def LS(): return list(input())
def SR(n): return [S() for _ in range(n)]
def SsR(n): return [Ss() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
sys.setrecursionlimit(10**6)
MOD = 10**9+7
INF = float('inf')


L, R = Is()
mod = 2019

n = min(R-L+1, 2019)
li = [-1]*n

tmp = L % 2019
for i in range(n):
    if tmp + i == 2019:
        print("0")
        exit()
    li[i] = tmp + i

ans = INF
for x, y in combinations(range(n), 2):
    ans = min(ans, li[x]*li[y]%mod)

print(ans)
