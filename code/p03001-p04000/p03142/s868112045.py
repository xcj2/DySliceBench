# coding:utf-8

import sys
from collections import deque, defaultdict
from operator import itemgetter

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


# def topological_sort(graph: list, indegree: list):
#     from collections import deque
#     que = deque(i for i in range(len(graph)) if indegree[i] == 0)
#     order = []
#     while que:
#         v = que.popleft()
#         order.append(v)
#         for next in graph[v]:
#             indegree[next] -= 1
#             if indegree[next] == 0:
#                 que.append(next)
#
#     return order


n, m = LI()

G = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(n + m - 1):
    a, b = LI_()
    G[a].append(b)
    indegree[b] += 1

que = deque()
for i in range(n):
    if indegree[i] == 0:
        que.append(i)
        break

ans = [0] * n
while que:
    v = que.popleft()
    for v2 in G[v]:
        indegree[v2] -= 1
        if indegree[v2] == 0:
            que.append(v2)
            ans[v2] = v + 1

print(*ans, sep='\n')
