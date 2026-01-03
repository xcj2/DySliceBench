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
from copy import deepcopy

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


n = I()
G = [[] for _ in range(n)]
win_against = [[] for _ in range(n)]
A = [-1]
for i in range(n - 1):
    a = I()
    A += [a - 1]
    win_against[a - 1] += [i + 1]

in_degree = [len(i) for i in win_against]
dp = [0] * n
dq = deque()
for i in range(n):
    if not in_degree[i]:
        dq += ([i])

order = []

while dq:
    x = dq.popleft()
    order += [x]
    if x == 0:
        break
    in_degree[A[x]] -= 1
    if in_degree[A[x]] == 0:
        dq += [A[x]]


for i in order:
    ret = 0
    s = sorted([dp[k] for k in win_against[i]])
    for l in range(1, len(win_against[i]) + 1):
        ret = max(ret, l + s.pop())
    dp[i] = ret

print(dp[0])
