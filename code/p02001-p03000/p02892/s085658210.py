from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007



n = I()
graph = SR(n)


def bfs(i):
    cost = [INF] * n
    cost[i] = 0
    que = deque([i])
    while que:
        cur = que.popleft()
        for nxt in range(n):
            if int(graph[cur][nxt]):
                c1 = cost[cur]
                if cost[nxt] != INF and cost[nxt] % 2 != (c1 + 1) % 2:
                    return -1
                else:
                    if cost[nxt] > c1 + 1:
                        cost[nxt] = c1 + 1
                        que += [nxt]
    return max(cost)



ret = 0
for j in range(n):
    if bfs(j) < 0:
        print(-1)
        break
    else:
        ret = max(ret, bfs(j))
else:
    print(ret + 1)