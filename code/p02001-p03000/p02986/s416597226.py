# verified: ABC014-D
# calculate LCA O(logN) for each query

# kprev[k][i]: 2^k parent of node i 
# if there is no node returns "None"
# Depth[i]: Depth of node i from rootNode

class Doubling():
    def __init__(self, graph, Depth, prev, rootNode=0):
        self.graph = graph
        self.N = len(graph)
        self.Log_N = (self.N-1).bit_length()
        self.rootNode = rootNode
        # BFSしない
        self.prev = prev 
        self.Depth = Depth

        # construct
        self.kprev = [self.prev]
        S = self.prev
        for k in range(self.Log_N):
            T = [None]*self.N
            for i in range(self.N):
                if S[i] is None:
                    continue
                T[i] = S[S[i]]
            self.kprev.append(T)
            S = T

    # LCA
    def LCAquery(self, u, v):
        dd = self.Depth[v] - self.Depth[u]
        if dd < 0:
            u, v = v, u
            dd = -dd
        
        # set same Depth
        for k in range(self.Log_N+1):
            if dd & 1:
                v = self.kprev[k][v]
            dd >>= 1
        
        if u == v:
            return u
        
        for k in reversed(range(self.Log_N)):
            pu = self.kprev[k][u]
            pv = self.kprev[k][v]
            if pu != pv:
                u, v = pu, pv
        
        return self.kprev[0][u]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from bisect import bisect_right

N, Q = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c, d = map(int, input().split())
    graph[a-1].append((b-1, c, d))
    graph[b-1].append((a-1, c, d))

Query = [list(map(int, input().split())) for _ in range(Q)]


D = [-1]*N
D[0] = 0
EulerTour = []
Color = [0]*N
Weight = [0]*N
PointFront = [-1]*N
prev = [None]*N
Depth = [0]*N
def dfs(p):
    PointFront[p] = len(EulerTour)
    EulerTour.append((p, +1))
    for np, c, d in graph[p]:
        if D[np] == -1:
            Color[np] = c
            Weight[np] = d
            D[np] = D[p] + d
            Depth[np] = Depth[p] + 1
            prev[np] = p
            dfs(np)
    EulerTour.append((p, -1))

def dfs2():
    stack = [0]
    while stack:
        p = stack[-1]
        if PointFront[p] == -1:
            PointFront[p] = len(EulerTour)
            EulerTour.append((p, +1))
        for np, c, d in graph[p]:
            if D[np] == -1:
                Color[np] = c
                Weight[np] = d
                D[np] = D[p] + d
                Depth[np] = Depth[p] + 1
                prev[np] = p
                stack.append(np)
        if p == stack[-1]:
            EulerTour.append((p, -1))    
            stack.pop()
            

#dfs(0)
dfs2()


Indexes = [[] for _ in range(N)]
Weights = [[0] for _ in range(N)]
Colors = [[0] for _ in range(N)]
for i, (p, num) in enumerate(EulerTour):
    if p == 0: continue
    w = Weight[p]*num
    c = Color[p]
    Weights[c].append(Weights[c][-1]+w)
    Colors[c].append(Colors[c][-1]+num)
    Indexes[c].append(i)



# point までにある color 指定された時のスコア
def fixed_score(point, color, replace):
    ind = bisect_right(Indexes[color], PointFront[point])
    return D[point] - Weights[color][ind] + Colors[color][ind]*replace


def main():
    doubling = Doubling(graph, Depth, prev)
    ans = []
    for x, y, u, v in Query:
        u -= 1; v -= 1
        lca = doubling.LCAquery(u, v)
        ans.append(fixed_score(u, x, y) + fixed_score(v, x, y) - 2*fixed_score(lca, x, y))
    print(*ans, sep="\n")

if __name__ == "__main__":
    main()