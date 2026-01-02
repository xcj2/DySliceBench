import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
def bfs(u, n, g):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

N, X, Y =MI()
E = [[] for _ in range(N + 1)]
for i in range(1, N):
    a = i
    b = i + 1
    E[a].append(b)
    E[b].append(a)
E[X].append(Y)
E[Y].append(X)

dist = [0] * N

for i in range(1, N + 1):
    D = deque(bfs(i, N + 1, E))
    D.popleft()
    for d in D:
        dist[d] += 1

for i in range(1, N):
    print(dist[i] // 2)