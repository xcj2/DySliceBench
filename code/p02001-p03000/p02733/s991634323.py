from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
from re import split
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy
import re

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

h, w, k = LI()
s = []
for _ in range(h):
    s += [[int(i) for i in list(S())]]
ans = INF
for j in range(2 ** (h - 1)):
    L = []
    last = 0
    for m in range(h - 1):
        if j >> m & 1:
            L += [(last, m + 1)]
            last = m + 1
    L += [(last, h)]
    now = [0] * len(L)
    last_x = 0
    cnt = len(L) - 1
    flag2 = 0
    flag = 0
    x = 0
    while x < w:
        flag3 = 0
        K = [s[y][x] for y in range(h)]
        for i in range(len(L)):
            l, r = L[i]
            k_sum = sum(K[l:r])
            if now[i] + k_sum > k:
                cnt += 1
                if flag == 0:
                    flag2 = 1
                    break
                else:
                    flag = 0
                    now = [0] * len(L)
                    flag3 = 1
                    break
            else:
                now[i] += k_sum
        else:
            flag = 1
        if flag3:
            continue
        if flag2:
            break
        x += 1
    else:
        ans = min(ans, cnt)


print(ans)
