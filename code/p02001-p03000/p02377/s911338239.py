import sys
readline = sys.stdin.readline

from heapq import heappop as hpp, heappush as hp
class MinCostFlowwithDijkstra:
    INF = 1<<31
    
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

N, M, F = map(int, readline().split())
T = MinCostFlowwithDijkstra(N)
for _ in range(M):
    u, v, cap, cost = map(int, readline().split())
    T.add_edge(u, v, cap, cost)

print(T.get_mf(0, N-1, F))
