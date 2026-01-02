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
from copy import deepcopy


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
mod = 998244353


n = I()
L = []
for i in range(n):
    l, r = LI()
    L += [(l, r, i)]

A = sorted(L, reverse=True)
B = sorted(L, key=lambda x:x[1])
used = [0] * n
now = 0
b_idx = 0
a_idx = 0
ans = 0
for i in range(n):
    if i % 2:
        while True:
            li, ri, idx = A[a_idx]
            if used[idx]:
                a_idx += 1
            else:
                used[idx] = 1
                break
        if li <= now <= ri:
            continue
        elif ri < now:
            ans += now - ri
            now = ri
        else:
            ans += li - now
            now = li
    else:
        while True:
            li, ri, idx = B[b_idx]
            if used[idx]:
                b_idx += 1
            else:
                used[idx] = 1
                break
        if li <= now <= ri:
            continue
        elif now < li:
            ans += li - now
            now = li
        else:
            ans += now - ri
            now = ri
ans += abs(now)
used = [0] * n
now = 0
ans1 = ans
b_idx = 0
a_idx = 0
ans2 = 0
for i in range(n):
    if i % 2 == 0:
        while True:
            li, ri, idx = A[a_idx]
            if used[idx]:
                a_idx += 1
            else:
                used[idx] = 1
                break
        if li <= now <= ri:
            continue
        elif ri < now:
            ans2 += now - ri
            now = ri
        else:
            ans2 += li - now
            now = li
    else:
        while True:
            li, ri, idx = B[b_idx]
            if used[idx]:
                b_idx += 1
            else:
                used[idx] = 1
                break
        if li <= now <= ri:
            continue
        elif now < li:
            ans2 += li - now
            now = li
        else:
            ans2 += now - ri
            now = ri
ans2 += abs(now)

print(max(ans1, ans2))






