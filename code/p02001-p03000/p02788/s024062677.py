from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from copy import deepcopy
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 20
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

n, d, a = LI()
X = []
H = []
xh = LIR(n)
xh.sort()
for x, h in xh:
    X += [x]
    H += [h]

X2 = [0] * n
ret = 0
ans = 0
for i in range(n):
    x = X[i]
    ret -= X2[i]
    remain = H[i] - ret
    if remain > 0:
        j = remain // a + bool(remain % a)
        ans += j
        ret += j * a
        if x + d * 2 < X[-1]:
            l = i
            r = n
            while l + 1 < r:
                mid = (l + r) // 2
                if X[mid] <= x + d * 2:
                    l = mid
                else:
                    r = mid
            X2[r] += j * a


print(ans)