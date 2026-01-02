from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, atan2, degrees
from operator import mul
from functools import reduce
sys.setrecursionlimit(10**8)

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


n = I()
A = LI()
total_xor = 0
for i in range(n):
    total_xor ^= A[i]


for i in range(n):
    A[i] &= ~total_xor


r = 0
for i in range(60, -1, -1):
    for j in range(r, n):
        if (A[j] >> i) & 1:
            A[r], A[j] = A[j], A[r]
            break
    else:
        continue
    for j in range(n):
        if j == r:
            continue
        if (A[j] >> i) & 1:
            A[j] ^= A[r]
    r += 1


ret = 0
for i in range(n):
    ret ^= A[i]


print(ret * 2 + total_xor)





