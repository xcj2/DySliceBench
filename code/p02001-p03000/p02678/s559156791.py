import sys
from collections import deque

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, M = LI()
G = [[] for _ in range(N+1)] # 隣接リスト

for _ in range(M):
    a, b = LI()
    G[a].append(b)
    G[b].append(a)

par = [None] * (N + 1)
# uからの距離
def bfs(u):
    queue = deque([u])
    d = [None] * (N+1)
    
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in G[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                par[i] = v
                queue.append(i)
    return d

d = bfs(1)
print('Yes')
print(*par[2:], sep='\n')

