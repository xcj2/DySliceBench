from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, acos, asin, atan, sqrt, tan, cos, pi
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(10 ** 7)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 998244353

s = S()
D = defaultdict(int)
for i in s:
    D[i]+=1

ans = len(s) * (len(s) - 1) // 2
for j in D.values():
    ans -= j * (j - 1) // 2

print(ans + 1)







