import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
from collections import *

class FordFulkerson:
    def __init__(self, N, edges):
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

N = int(input())
edges = []

for i in range(1, N+1):
    edges.append((0, i, 1))

for i in range(N+1, 2*N+1):
    edges.append((i, 2*N+1, 1))

ab = [tuple(map(int, input().split())) for _ in range(N)]
cd = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if ab[i][0]<cd[j][0] and ab[i][1]<cd[j][1]:
            edges.append((1+i, N+1+j, 1))

ff = FordFulkerson(2*N+2, edges)
print(ff.max_flow(0, 2*N+1))