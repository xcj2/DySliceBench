from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy

sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def FI(): return list(map(float, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): pass
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


n = I()
A = LI()
memo  = [[[-1.0] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
memo[0][0][0] = 0
def f(i, j, k):
    if memo[i][j][k] != -1:
        return memo[i][j][k]
    s = i + j + k
    ret = n - s
    if i:
        ret += i * (f(i - 1, j, k) + 1)
    if j:
        ret += j * (f(i + 1, j - 1, k) + 1)
    if k:
        ret += k * (f(i, j + 1, k - 1) + 1)
    memo[i][j][k] = ret / s
    return memo[i][j][k]

one, two, three = 0, 0, 0
for i in range(n):
    if A[i] == 1:
        one += 1
    elif A[i] == 2:
        two += 1
    else:
        three += 1

print(f(one, two, three))