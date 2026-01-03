import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000)
from collections import *

class FordFulkerson:
    def __init__(self, N, edges): #edges: (s, t, c) sからtに向かう容量cの有向辺
        self.N = N
        self.G = defaultdict(lambda : defaultdict(int))
        
        for s, t, cap in edges:
            self.G[s][t] = cap
        
    def dfs(self, v, t, f):
        if v==t:
            return f
        
        self.used[v] = True
        
        for nv, cap in self.G[v].items():
            if not self.used[nv] and self.G[v][nv]>0:
                d = self.dfs(nv, t, min(f, self.G[v][nv]))
                
                if d>0:
                    self.G[v][nv] -= d
                    self.G[nv][v] += d
                    
                    return d
        
        return 0
    
    def max_flow(self, s, t):
        flow = 0
        
        while True:
            self.used = [False]*self.N
            f = self.dfs(s, t, 10**18)
        
            if f==0:
                return flow
        
            flow += f

H, W = map(int, input().split())
a = [list(input()[:-1]) for _ in range(H)]

for i in range(H):
    for j in range(W):
        if a[i][j]=='S':
            sx, sy = i, j
        
        if a[i][j]=='T':
            tx, ty = i, j

if sx==tx or sy==ty:
    print(-1)
    exit()
    
edges = []
edges.append((0, sx+1, 10**18))
edges.append((0, H+sy+1, 10**18))
edges.append((tx+1, H+W+1, 10**18))
edges.append((H+ty+1, H+W+1, 10**18))

for i in range(H):
    for j in range(W):
        if a[i][j]=='o':
            edges.append((i+1, H+j+1, 1))
            edges.append((H+j+1, i+1, 1))
    
ff = FordFulkerson(H+W+2, edges)
print(ff.max_flow(0, H+W+1))