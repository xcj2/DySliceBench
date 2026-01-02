#GRL_3_C
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def scc():
    order = []
    visited = [False]*N
    
    def dfs(v):
        visited[v] = True
        
        for nv in G[v]:
            if not visited[nv]:
                dfs(nv)
        
        order.append(v)
    
    for i in range(N):
        if not visited[i]:
            dfs(i)
    
    visited = [False]*N
    group = [-1]*N
    label = 0
    
    def rdfs(v, label):
        group[v] = label
        visited[v] = True
        
        for nv in RG[v]:
            if not visited[nv]:
                rdfs(nv, label)
    
    for v in reversed(order):
        if not visited[v]:
            rdfs(v, label)
            label += 1
            
    return label, group

N, M = map(int, input().split())
G = [[] for _ in range(N)]
RG = [[] for _ in range(N)]

for _ in range(M):
    s, t = map(int, input().split())
    G[s].append(t)
    RG[t].append(s)
    
_, group = scc()

Q = int(input())

for _ in range(Q):
    u, v = map(int, input().split())
    
    if group[u]==group[v]:
        print(1)
    else:
        print(0)
