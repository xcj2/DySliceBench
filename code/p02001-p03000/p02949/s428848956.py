# Coins Respawn
import sys
sys.setrecursionlimit(10**7)
from collections import deque
N, M, P = map(int, input().split())
graph = []
d = deque()

# グラフの整形

from_1 = [[] for i in range(N+1)]
from_N = [[] for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    from_1[a].append(b)
    from_N[b].append(a)
    d.append((a, b, P-c))


accessible_1 = [False for i in range(N+1)]
accessible_N = [False for i in range(N+1)]


def dfs_1(s):
    accessible_1[s] = True
    for node in from_1[s]:
        if accessible_1[node] == False:
            dfs_1(node)


def dfs_N(s):
    accessible_N[s] = True
    for node in from_N[s]:
        if accessible_N[node] == False:
            dfs_N(node)


dfs_1(1)
dfs_N(N)

isok = [False for i in range(N+1)]
for i in range(N+1):
    if accessible_1[i] and accessible_N[i]:
        isok[i] = True


while d:
    p, q, weight = d.popleft()
    if isok[p] and isok[q]:
        graph.append((p, q, weight))

# ベルマンフォード


def bellman_ford(s,n):
    dist = [10**20 for i in range(n+1)]
    dist[s] = 0
    for i in range(1, n+1):
        flag = False
        for some in graph:
            a, b, d = some[0], some[1], some[2]
            newlen = dist[a]+d
            if newlen < dist[b]:
                flag = True
                dist[b] = newlen
        if not flag:
            break
        if i == n:
            return False
    return dist

K=bellman_ford(1,N)
if K==False:
     print(-1)
else:
    print(max(0,-K[N]))