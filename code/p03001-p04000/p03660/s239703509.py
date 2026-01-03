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


INF = float('inf')
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
mod = 1000000007


n = I()
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = LI()
    graph[a - 1] += [b - 1]
    graph[b - 1] += [a - 1]




f_que = deque([0])
s_que = deque([n - 1])
visited = [0] * n
visited[0] = 1
visited[n - 1] = 1
f_cnt = s_cnt = 0
while f_que or s_que:
    f_tmp = deque()
    for cur in f_que:
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            f_tmp += [nxt]
            visited[nxt] = 1
            f_cnt += 1
    f_que = f_tmp
    s_tmp = deque()
    for cur in s_que:
        for nxt in graph[cur]:
            if visited[nxt]:
                continue
            s_tmp += [nxt]
            visited[nxt] = 1
            s_cnt += 1
    s_que = s_tmp


if s_cnt >= f_cnt:
    print('Snuke')
else:
    print('Fennec')