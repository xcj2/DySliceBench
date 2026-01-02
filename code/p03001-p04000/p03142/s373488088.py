# coding:utf-8

import sys
from collections import deque
from operator import itemgetter

INF = float('inf')
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, m = LI()

G = [[] for _ in range(n)]
RG = [[] for _ in range(n)]
indegree = [0] * n

for _ in range(n + m - 1):
    a, b = LI_()
    G[a].append(b)
    RG[b].append(a)
    indegree[b] += 1

# Topological sort
que = deque()
for i in range(n):
    if indegree[i] == 0:
        que.append(i)

res = []
while que:
    v = que.popleft()
    res.append(v)
    for v2 in G[v]:
        indegree[v2] -= 1
        if indegree[v2] == 0:
            que.append(v2)

# 親の候補が複数ある場合
# 木の高さが最大になるような候補を選ぶ
# -> トポロジカル順序で最も後ろにある候補を選ぶ
order = [i for i, n in sorted(enumerate(res), key=itemgetter(1))]
for i in range(n):
    if len(RG) == 0:
        print(0)
        continue

    parent = -1
    d = -1
    for j in RG[i]:
        if order[j] > d:
            parent = j
            d = order[j]

    print(parent + 1)
