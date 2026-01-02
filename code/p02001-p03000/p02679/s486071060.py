from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, cos, radians, pi, sin, gcd
from operator import mul
from functools import reduce
from operator import mul


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
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
D = defaultdict(int)
A = []
B = []
F = []
pow2 = [1] * (n + 1)
for i in range(1, n + 1):
    pow2[i] = pow2[i - 1] * 2 % mod

ans = 1
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in range(n):
    a, b = LI()
    flg = 0
    if a * b < 0:
        flg = 1
    a = abs(a)
    b = abs(b)
    g = gcd(a, b)
    if g:
        a = a // g
        b = b // g
    A += [a]
    B += [b]
    F += [flg]
    if a == 0 and b == 0:
        cnt3 += 1
    elif a == 0:
        cnt1 += 1
    elif b == 0:
        cnt2 += 1
    else:
        D[(flg, a, b)] += 1

visited = defaultdict(int)
for j in range(n):
    fi, ai, bi = F[j], A[j], B[j]
    if ai == 0 or bi == 0:
        continue
    if visited[(fi, ai, bi)]:
        continue
    visited[(fi, ai, bi)] = 1
    visited[(fi ^ 1, bi, ai)] = 1
    ans = ans * (pow2[D[(fi, ai, bi)]] + pow2[D[(fi ^ 1, bi, ai)]] - 1) % mod

print((ans * (pow2[cnt1] + pow2[cnt2] - 1) + cnt3 - 1) % mod)
