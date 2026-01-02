from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce



INF = float('inf')
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
mod = 1000000007



n,k,q=LI()
L=[k-q] * n
A = IR(q)



for l in A:
    L[l-1]+=1



for j in range(n):
    if L[j] > 0:
        print('Yes')
    else:
        print('No')