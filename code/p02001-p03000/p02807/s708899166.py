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
INF = float('INF')
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
mod = 10 ** 9 + 7


n = I()
X = LI()
d = [0] * (n - 1)
for i in range(n - 1):
    d[i] = (X[i + 1] - X[i]) % mod



fac = [1] * (n + 1)
inv = [1] * (n + 1)
for j in range(1, n + 1):
    fac[j] = fac[j-1] * j % mod



for i in range(1, n):
    inv[i] = pow(i, mod - 2, mod)




L = [fac[n - 1] * inv[i] % mod for i in range(1, n)]
for k in range(1, n - 1):
    L[k] = (L[k] + L[k - 1]) % mod




ret = 0
for j in range(n - 1):
    ret = (ret + L[j] * d[j] % mod) % mod


print(ret % mod)






