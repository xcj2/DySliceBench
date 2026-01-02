from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


n, m = LI()
L = LIR(m)
for i in range(m):
    L[i] = [i, str(L[i][0]).zfill(6), L[i][1]]


L.sort(key=lambda x:x[1:])
cnt = 1
L[0][2] = str(1).zfill(6)
for i in range(1, m):
    if L[i][1] != L[i-1][1]:
        cnt = 1
    else:
        cnt += 1
    L[i][2] = str(cnt).zfill(6)



L.sort(key=lambda x:x[0])
for i in L:
    print(i[1] + i[2])