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
sys.setrecursionlimit(10 ** 9)



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
A = LI()
graph = [[] for _ in range(n)]
for u, v in LIR(n - 1):
    graph[u - 1] += [v - 1]
    graph[v - 1] += [u - 1]

if n == 2:
    x, y = A
    answer = 'YES' if x == y else 'NO'
    print(answer)
    exit()


def dfs(v, parent=None):
    x = A[v]
    if len(graph[v]) == 1:
        return x
    s = 0
    for w in graph[v]:
        if w == parent:
            continue
        ret = dfs(w, v)
        if ret == None:
            return None
        if x < ret:
            print('NO')
            exit()
        s += ret
    if 2 * x - s > s:
        print('NO')
        exit()
    if 2 * x < s:
        print('NO')
        exit()
    return 2 * x - s


v=0
while len(graph[v]) == 1:
    v += 1

if not dfs(v):
    print('YES')
else:
    print('NO')
