import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import deque

N,*A = map(int,read().split())

class Dinic:
    def __init__(self, N, source, sink):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.source = source
        self.sink = sink

    def add_edge(self, fr, to, cap):
        n1 = len(self.G[fr])
        n2 = len(self.G[to])
        self.G[fr].append([to, cap, n2])
        self.G[to].append([fr, 0, n1]) # 逆辺を cap 0 で追加
        
    def add_edge_undirected(self, fr, to, cap):
        n1 = len(self.G[fr])
        n2 = len(self.G[to])
        self.G[fr].append([to, cap, n2])
        self.G[to].append([fr, cap, n1])
        
    def bfs(self):
        level = [0] * self.N
        G = self.G; source = self.source; sink = self.sink
        q = deque([source])
        level[source] = 1
        pop = q.popleft; append = q.append
        while q:
            v = pop()
            lv = level[v] + 1
            for to, cap, rev in G[v]:
                if not cap:
                    continue
                if level[to]:
                    continue
                level[to] = lv
                if to == sink:
                    self.level = level
                    return
                append(to)
        self.level = level
        
    def dfs(self,v,f):
        if v == self.sink:
            return f
        G = self.G
        prog = self.progress
        level = self.level
        lv = level[v]
        E = G[v]
        for i in range(prog[v],len(E)):
            to, cap, rev = E[i]
            prog[v] = i
            if not cap:
                continue
            if level[to] <= lv:
                continue
            x = f if f < cap else cap
            ff = self.dfs(to, x)
            if ff:
                E[i][1] -= ff
                G[to][rev][1] += ff
                return ff
        return 0
    
    def max_flow(self):
        INF = 10**18
        flow = 0
        while True:
            self.bfs()
            if not self.level[self.sink]:
                return flow
            self.progress = [0] * self.N
            while True:
                f = self.dfs(self.source, INF)
                if not f:
                    break
                flow += f
        return flow

source = 0; sink = N+1; INF = 10 ** 18
dinic = Dinic(N+2,source,sink)
add = dinic.add_edge

for i,x in enumerate(A,1):
    if x < 0:
        # source側：割るものを表現。sink側にうつすときにカット-xが必要。
        add(source,i,-x)
    else:
        # sink側：割らないものを表現。source側にうつすときにカットxが必要。
        add(i,sink,x)

for i in range(1,N+1):
    for j in range(i+i,N+1,i):
        # iを割るならjも割る。iを割ってjを割らないのは禁止
        # iがsourceでjがsinkなのは禁止
        add(i,j,INF)

f = dinic.max_flow()
x = sum(x for x in A if x >= 0)
answer = x - f

print(answer)