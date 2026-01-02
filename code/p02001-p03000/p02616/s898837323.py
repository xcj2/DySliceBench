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
mod = 10 ** 9 + 7


n, k = LI()
A = LI()
A.sort()
if k % 2 and all([a < 0 for a in A]):
    ret = 1
    A.reverse()
    for i in range(k):
        ret = ret * A[i] % mod
    print(ret)
    exit()

i = 0
ret = A.pop() if k % 2 else 1
while k > 1:
    x = A[i] * A[i + 1]
    y = A[-1] * A[-2]
    if y > x:
        A.pop()
        A.pop()
        ret = ret * y % mod
    else:
        ret = ret * x % mod
        i += 2
    k -= 2
    ret %= mod

print(ret)



