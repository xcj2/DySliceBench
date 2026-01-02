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
s = SRL(h)
ans = INF
for bits in range(2 ** (h - 1)):
    res = sum([int(j) for j in "{0:b}".format(bits)])
    div_cnt = res + 1
    cnt = [0] * div_cnt
    x = 0
    flg = 0
    while x < w:
        cur = 0
        for y in range(h):
            if s[y][x] == '1':
                cnt[cur] += 1
            if bits >> y & 1:
                cur += 1
        if max(cnt) > k:
            if flg == 0:
                res = INF
                break
            else:
                cnt = [0] * div_cnt
                flg = 0
                res += 1
        else:
            flg = 1
            x += 1
    ans = min(ans, res)


print(ans)



