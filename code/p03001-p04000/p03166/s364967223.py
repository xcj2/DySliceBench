# coding:utf-8

import sys
from collections import defaultdict, deque

INF = 10 ** 5
MOD = 10 ** 9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()


n, m = LI()

G = defaultdict(list)
G2 = defaultdict
in_degree = [0] * n
for _ in range(m):
    x, y = LI_()
    G[x].append(y)
    in_degree[y] += 1

# トポロジカルソート
q = deque()
for v, e in enumerate(in_degree):
    if e == 0:
        q.append(v)

res = []
while q:
    v = q.popleft()
    res.append(v)
    for nv in G[v]:
        in_degree[nv] -= 1
        if in_degree[nv] == 0:
            q.append(nv)

dp = [0] * n
for v in res:
    for nv in G[v]:
        dp[nv] = max(dp[nv], dp[v] + 1)

print(max(dp))
