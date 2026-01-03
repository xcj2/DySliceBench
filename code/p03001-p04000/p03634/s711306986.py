from collections import defaultdict, deque
from heapq import heappush, heappop, heapify
import math
import bisect
import random
import sys


def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
mod = 1000000007


n = I()
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1] += [[b-1, c]]
    graph[b-1] += [[a-1, c]]



q, k = LI()
q_ab = LIRM(q)



dist = n * [-1]
dist[k-1] = 0
que = deque([k-1])
while que:
    cur = que.pop()
    for nxt, c in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + c
            que += [nxt]



for a, b in q_ab:
    print(dist[a] + dist[b])