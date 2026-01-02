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


n, c = LI()
D = LIR(c)
C = LIR(n)
#　mod_color[mod3][color]
mod_color = [[0] * c for _ in range(3)]
for y in range(n):
    for x in range(n):
        mod_color[(y + x + 2) % 3][C[y][x] - 1] += 1


# 30 * 29 * 28
ans = INF
for i in range(c):
    for j in range(c):
        if j == i: continue
        for k in range(c):
            if k == i or k == j: continue
# もともとmod0のところをiに、mod1のところをjに、mod2のところをkにする。
            ret = 0
            for l in range(3):
                for m in range(c):
                    if l == 0:
                        ret += mod_color[l][m] * D[m][i]
                    elif l == 1:
                        ret += mod_color[l][m] * D[m][j]
                    else:
                        ret += mod_color[l][m] * D[m][k]
            ans = min(ans, ret)


print(ans)

