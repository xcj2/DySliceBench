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
from operator import mul
from functools import reduce
from operator import mul


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
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
A = LI()



D = defaultdict(int)
for i in range(n):
    a = A[i]
    Di = defaultdict(int)
    for j in range(2, int(a ** 0.5) + 1):
        while a % j == 0:
            a //= j
            Di[j] += 1
    if a:
        Di[a] += 1
    for k in Di:
        D[k] = max(D[k], Di[k])

ret = 1
for ki in D:
    ret = ret * pow(ki, D[ki], mod)
    ret %= mod

ans = 0
for a in A:
    ans += ret * pow(a, mod - 2, mod)
    ans %= mod

print(ans)




