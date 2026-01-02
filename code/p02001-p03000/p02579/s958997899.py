from heapq import heappush, heappop
inf = float('inf')
def dijkstra(graph:list, node:int, start:int) -> list:
    # graph[node] = [(cost, to)]
    dist = [inf]*node

    dist[start] = 0
    heap = [(0,start)]
    while heap:
        cost,thisNode = heappop(heap)
        for NextCost,NextNode in graph[thisNode]:
            dist_cand = dist[thisNode]+NextCost
            if dist_cand < dist[NextNode]:
                dist[NextNode] = dist_cand
                heappush(heap,(dist[NextNode],NextNode))
    return dist

class UnionFind:
    def __init__(self, num):
        self.table = [-1 for _ in range(num)]

    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)

        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False

H,W = map(int,input().split())
Ch,Cw = map(int,input().split())
Dh,Dw = map(int,input().split())
S = [input() for _ in range(H)]

Ch -= 1
Cw -= 1
Dh -= 1
Dw -= 1

u = UnionFind(H*W)
for sh in range(H):
    for sw in range(W):
        if S[sh][sw]=='#':
            continue
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if 0<=sh+dx<=H-1 and 0<=sw+dy<=W-1 and S[sh+dx][sw+dy]=='.':
                    u.union(sh*W+sw,(sh+dx)*W+sw+dy)
d = {}
n = 0
for sh in range(H):
    for sw in range(W):
        f = u.find(sh*W+sw)
        if f not in d:
            d[f] = n
            n += 1

graph = [[] for _ in range(len(d))]
for sh in range(H):
    for sw in range(W):
        if S[sh][sw]=='#':
            continue
        f1 = u.find(sh*W+sw)
        for dx in range(-2,3):
            for dy in range(-2,3):
                if 0<=sh+dx<=H-1 and 0<=sw+dy<=W-1 and S[sh+dx][sw+dy]=='.':
                        f2 = u.find((sh+dx)*W+sw+dy)
                        graph[d[f1]].append((1,d[f2]))

dist = dijkstra(graph, len(d), d[u.find(Ch*W+Cw)])
ans = dist[d[u.find(Dh*W+Dw)]]
if ans == inf:
    ans = -1
print(ans)