import sys
from collections import Counter

sys.setrecursionlimit(10**7)
 
inf = 1<<100
 
def solve():
    N, M = map(int, input().split())
    edges = [None]*M
    Adj = [[] for i in range(N)]
 
    for i in range(M):
        ui, vi, ci = map(int, sys.stdin.readline().split())
        ui, vi = ui - 1, vi - 1
        edges[i] = (ui, vi, -ci)
        Adj[ui].append(vi)

    visitable = [False]*N

    dfs(N, M, Adj, visitable, 0)

    reachable = [False]*N
    reachable[0] = True
    reachable[N - 1] = True

    for u in range(1, N - 1):
        visited = [False]*N

        dfs(N, M, Adj, visited, u)

        if visited[N - 1]:
            reachable[u] = True
 
    ans = Bellmanford(N, M, edges, visitable, reachable)
 
    if ans is not None:
        print(-ans)
    else:
        print('inf')

def dfs(N, M, Adj, visitable, u):
    visitable[u] = True

    for v in Adj[u]:
        if not visitable[v]:
            dfs(N, M, Adj, visitable, v)

def Bellmanford(N, M, edges, visitable, reachable):
    dist = [inf]*N
    dist[0] = 0
    flag = True

    cnt = 0
 
    for i in range(N):
        flag = False

        for (u, v, c) in edges:
            if dist[u] != inf and dist[v] > dist[u] + c:
                dist[v] = dist[u] + c

                if visitable[v] and reachable[v]:
                    flag = True

        # print(dist)

        if not flag:
            break

        if flag and i == N - 1:
            return None

    return dist[N - 1]
 
if __name__ == '__main__':
    solve()