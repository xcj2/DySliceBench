import sys
readline = sys.stdin.readline

import collections
class Dinic:
    def __init__(self, vnum):
        self.edge = [[] for i in range(vnum)]
        self.n = vnum
        # infはint型の方が良いかもね
        self.inf = float('inf')
    def addedge(self, st, en, c):
        self.edge[st].append([en, c, len(self.edge[en])])
        self.edge[en].append([st, 0, len(self.edge[st])-1])
    def bfs(self, vst):
        dist = [-1]*self.n
        dist[vst] = 0
        Q = collections.deque([vst])
        while Q:
            nv = Q.popleft()
            for vt, c, r in self.edge[nv]:
                if dist[vt] == -1 and c > 0:
                    dist[vt] = dist[nv] + 1
                    Q.append(vt)
        self.dist = dist
    def dfs(self, nv, en, nf):
        nextv = self.nextv
        if nv == en:
            return nf
        dist = self.dist
        ist = nextv[nv]
        for i, (vt, c, r) in enumerate(self.edge[nv][ist:], ist):
            if dist[nv] < dist[vt] and c > 0:
                df = self.dfs(vt, en, min(nf, c))
                if df > 0:
                    self.edge[nv][i][1] -= df
                    self.edge[vt][r][1] += df
                    return df
            nextv[nv] += 1
        return 0
    def getmf(self, st, en):
        mf = 0
        while True:
            self.bfs(st)
            if self.dist[en] == -1:
                break
            self.nextv = [0]*self.n
            while True:
                fl = self.dfs(st, en, self.inf)
                if fl > 0:
                    mf += fl
                else:
                    break
        return mf
    
    #二部グラフのマッチング復元の時はsinkとつながってる辺のうち容量が０でなくsink出ない辺の先がマッチング対象

from heapq import heappop as hpp, heappush as hp
class MinCostFlowwithDijkstra:
    INF = 1<<60
    
    def __init__(self, N):
        self.N = N
        self.Edge = [[] for _ in range(N)]
    
    def add_edge(self, st, en, cap, cost):
        self.Edge[st].append([en, cap, cost, len(self.Edge[en])])
        self.Edge[en].append([st, 0, -cost, len(self.Edge[st])-1])
    
    def get_mf(self, so, si, fl):
        N = self.N
        INF = self.INF
        res = 0
        Pot = [0]*N
        geta = N
        
        
        prv = [None]*N
        prenum = [None]*N
        while fl:
            dist = [INF]*N
            dist[so] = 0
            Q = [so]
            
            while Q:
                cost, vn = divmod(hpp(Q), geta)
                if dist[vn] < cost:
                    continue
                
                for enum in range(len(self.Edge[vn])):
                    vf, cap, cost, _ = self.Edge[vn][enum]
                    cc = dist[vn] + cost - Pot[vn] + Pot[vf]
                    if cap > 0 and dist[vf] > cc:
                        dist[vf] = cc
                        prv[vf] = vn
                        prenum[vf] = enum
                        hp(Q, cc*geta + vf)
            
            if dist[si] == INF:
                return -1
            
            for i in range(N):
                Pot[i] -= dist[i]
            
            cfl = fl
            vf = si
            while vf != so:
                cfl = min(cfl, self.Edge[prv[vf]][prenum[vf]][1])
                vf = prv[vf]
            
            fl -= cfl
            res -= cfl*Pot[si]
            vf = si
            while vf != so:
                e = self.Edge[prv[vf]][prenum[vf]]
                e[1] -= cfl
                self.Edge[vf][e[3]][1] += cfl
                vf = prv[vf]
        return res

N, M = map(int, readline().split())

G = []

wall = ord('#')
st = ord('o')
S = []
css = 0
for i in range(N):
    k = list(map(ord, readline().strip()))
    res = []
    for j in range(M):
        if k[j] == st:
            S.append((i, j))
            css += 1
        if k[j] == wall:
            res.append(1)
        else:
            res.append(0)
    G.append(res)

geta1 = N*M
geta2 = M
so = 2*N*M
si = so + 1
FF = MinCostFlowwithDijkstra(2*N*M+2)

INF = 10**9+7
for i, j in S:
    stack = [(i, j)]
    used = set((i, j))
    FF.add_edge(so, i*geta2+j, 1, 0)
    FF.add_edge(i*geta2+j, geta1+i*geta2+j, 1, INF)
    while stack:
        vi, vj = stack.pop()
        for di, dj in ((1, 0), (0, 1)):
            fi, fj = vi+di, vj+dj
            if 0 <= fi < N and 0 <= fj < M and not G[fi][fj]:
                if (fi, fj) not in used:
                    used.add((fi, fj))
                    stack.append((fi, fj))
                    cost = INF - (fi-i) - (fj-j)
                    FF.add_edge(i*geta2+j, geta1+fi*geta2+fj, 1, cost)

for i in range(N):
    for j in range(M):
        if G[i][j]:
            continue
        FF.add_edge(geta1+i*geta2+j, si, 1, 0)

print(css*INF-FF.get_mf(so, si, css))
    