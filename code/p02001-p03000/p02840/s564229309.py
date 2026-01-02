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
import pprint
sys.setrecursionlimit(10 ** 9)


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



n, x, d = LI()
if d == 0:
    if x == 0:
        print(1)
    else:
        print(n + 1)
    exit()

D = defaultdict(list)
for i in range(n + 1):
    a = i * x
    L = i * (i - 1) // 2
    R = (2 * n - i - 1) * i // 2
    D[a % d] += [(a // d + L, a // d + R)]


ans = 0
for L in D.values():
    L.sort()
    now = -INF
    for l, r in L:
        if r <= now:
            continue
        elif l > now:
            ans += r - l + 1
        else:
            ans += r - now
        now = r


print(ans)
