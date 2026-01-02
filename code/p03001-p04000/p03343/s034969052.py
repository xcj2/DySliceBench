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


sys.setrecursionlimit(2147483647)
INF = 1 << 100
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


n, k, q = LI()
A = LI()


def list_split(arr, x):
    ret = []
    d = []
    for v in arr:
        if v >= x:
            d += [v]
        elif d:
            ret += [d]
            d = []
    else:
        ret += [d]
    return ret


ans = INF
for e in set(A):
    y = []
    for arr in list_split(A, e):
        l = len(arr)
        if l >= k:
            y += sorted(arr)[:min(l - k + 1, q)]
    if len(y) >= q:
        ans = min(ans, sorted(y)[q - 1] - e)



print(ans)


