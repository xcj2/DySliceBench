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


# https://atcoder.jp/contests/abc152/submissions/9619555

import sys
readline = sys.stdin.readline



n = I()
G = [[] for _ in range(n)]
for i in range(n - 1):
    u, v = LI()
    G[u - 1] += [(i, v - 1)]
    G[v - 1] += [(i, u - 1)]


def dfs(root):
    q = [root]
    path_bit = [-1] * n
    path_bit[root] = 0
    while q:
        u = q.pop()
        for i, v in G[u]:
            if path_bit[v] != -1:
                continue
            path_bit[v] = path_bit[u] | 1 << i
            q += [v]
    return path_bit



def popcnt(n):
    c = (n & 0x5555555555555555) + ((n >> 1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c >> 2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c >> 4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c >> 8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c >> 16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c >> 32) & 0x00000000ffffffff)
    return c


m = I()
cond = LIR(m)
path_bit = dfs(0)
cond_bit = [0] * m
for j, (u, v) in enumerate(cond):
    cond_bit[j] = path_bit[u - 1] ^ path_bit[v - 1]

L = [0] * (2 ** m)
C = [0] * n
for i in range(2 ** m):
    if i != 0:
        L[i] = L[(i ^ (i & -i))] | cond_bit[(i & -i).bit_length() - 1]
# それぞれの条件を満たさないものを全事象から引く。
# 次に、2個同時に条件を満たさないものをたす。という要領。
    cond_cnt = popcnt(i)
# p_cnt が満たさない条件の数。
    if cond_cnt % 2:
        C[n - 1 - popcnt(L[i])] -= 1
    else:
        C[n - 1 - popcnt(L[i])] += 1


ans = 0
for i in range(n):
    ans += 2 ** i * C[i]


print(ans)