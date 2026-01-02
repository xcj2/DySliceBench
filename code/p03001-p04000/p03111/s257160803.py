from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left


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


n, a, b, c = LI()
L = IR(n)


def recur(ai, bi, ci, i):
    if i == n:
        return abs(a - ai) + abs(b -bi) + abs(c - ci) - 30 if ai > 0 and bi > 0 and ci > 0 else INF
    l1 = recur(ai + L[i], bi, ci, i+1) + 10
    l2 = recur(ai, bi + L[i], ci, i+1) + 10
    l3 = recur(ai, bi, ci + L[i], i+1) + 10
    l4 = recur(ai, bi, ci, i+1)
    return min(l1, l2, l3, l4)



print(recur(0, 0, 0, 0))