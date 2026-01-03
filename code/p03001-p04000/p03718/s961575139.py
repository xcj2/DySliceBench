import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import defaultdict

H,W = map(int,readline().split())
A = [line.rstrip().decode('utf-8') for line in readlines()]

source = 0
sink = H+W+1

graph = [defaultdict(int) for _ in range(H+W+2)]

INF = 10 ** 18
for h in range(1,H+1):
    for w,ox in enumerate(A[h-1],1):
        if ox == 'x':
            continue
        elif ox == 'o':
            graph[h][H+w] = 1
            graph[H+w][h] = 1
        elif ox == 'S':
            graph[source][h] = INF
            graph[h][source] = INF
            graph[source][H+w] = INF
            graph[H+w][source] = INF
        elif ox == 'T':
            graph[sink][h] = INF
            graph[h][sink] = INF
            graph[sink][H+w] = INF
            graph[H+w][sink] = INF


class Dinic():
    def __init__(self,graph,V,source,sink):
        self.graph = graph
        self.sink = sink
        self.source = source
        self.V = V
#        self.compress()
        self.N = len(V)
    
    def compress(self):
        self.N = len(self.V)
        v_to_i = {x:i for i,x in enumerate(self.V)}
        self.sink = v_to_i[self.sink]
        self.source = v_to_i[self.source]
        g = [dict() for _ in range(self.N)]
        for v,e in self.graph.items():
            vn = v_to_i[v]
            g[vn] = {v_to_i[w]:c for w,c in e.items()}
        self.graph = g
        
    def bfs(self):
        level = [0]*self.N
        q = [self.source]
        level[self.source] = 1
        d = 1
        while q:
            if level[self.sink]:
                break
            qq = []
            d += 1
            for v in q:
                for w,cap in self.graph[v].items():
                    if cap == 0:
                        continue
                    if level[w]:
                        continue
                    level[w] = d
                    qq.append(w)
            q = qq
        self.level = level
        
    def dfs(self,v,f):
        if v == self.sink:
            return f
        for w,cap in self.itr[v]:
            if cap == 0 or self.level[w] != self.level[v] + 1:
                continue
            d = self.dfs(w,min(f,cap))
            if d:
                self.graph[v][w] -= d
                self.graph[w][v] += d
                return d
        return 0
    
    def max_flow(self):
        INF = 10**18
        flow = 0
        while True:
            self.bfs()
            if self.level[self.sink] == 0:
                break
            self.itr = [iter(e.items()) for e in self.graph]
            while True:
                f = self.dfs(self.source,INF)
                if f == 0:
                    break
                flow += f
        return flow

answer = Dinic(graph=graph,V=list(range(H+W+2)),source=0,sink=H+W+1).max_flow()
if answer >= INF:
    answer = -1
print(answer)