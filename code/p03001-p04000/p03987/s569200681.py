from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 18
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n = I()
A = [0] + LI() + [0]
val_ind = {A[j]: j for j in range(n + 2)}
l = {i:i - 1 for i in range(1, n + 1)}
r = {i:i + 1 for i in range(1, n + 1)}
ans = 0
for k in range(n, 0, -1):
    k_ind = val_ind[k]
    l1 = l[k_ind]
    r1 = r[k_ind]
    ans += (k_ind - l1) * (r1 - k_ind) * k
    r[l1] = r1
    l[r1] = l1



print(ans)