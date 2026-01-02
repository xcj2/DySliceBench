from itertools import product
from collections import deque

class ZeroOneBFS:
    def __init__(self, N):
        self.N = N # #vertices
        self.E = [[] for _ in range(N)]
        
    def add_edge(self, init, end, weight, undirected=False):
        assert weight in [0, 1]
        self.E[init].append((end, weight))
        if undirected: self.E[end].append((init, weight))
        
    def distance(self, s):
        INF = float('inf')
        E, N = self.E, self.N
        dist = [INF] * N # the distance of each vertex from s
        prev = [-1] * N # the previous vertex of each vertex on a shortest path from s
        dist[s] = 0
        dq = deque([(0, s)]) # (dist, vertex)
        n_visited = 0 # #(visited vertices)
        while dq:
            d, v = dq.popleft() 
            if dist[v] < d: continue # (s,v)-shortest path is already calculated
            for u, c in E[v]:
                temp = d + c
                if dist[u] > temp:
                    dist[u] = temp; prev[u] = v
                    if c == 0: dq.appendleft((temp, u))
                    else: dq.append((temp, u))
            n_visited += 1
            if n_visited == N: break
        self.dist, self.prev = dist, prev
        return dist
    
    def shortest_path(self, t):
        P = []
        prev = self.prev
        while True:
            P.append(t)
            t = prev[t]
            if t == -1: break
        return P[::-1]

H, W = map(int, input().split())
zobfs = ZeroOneBFS(H * W)
 
def vtx(i, j): return i*W + j
def coord(n): return divmod(n, W)
 
grid = [input() for _ in range(H)] # |string| = W
E = [[] for _ in range(H * W)]
ans = 0 if grid[0][0] == '.' else 1
for i, j in product(range(H), range(W)):
    v = vtx(i, j)
    check = [vtx(i+dx, j+dy) for dx, dy in [(1, 0), (0, 1)] if i+dx <= H-1 and j+dy <= W-1]
    for u in check:
        x, y = coord(u)
        if grid[i][j] == '.' and grid[x][y] == '#':
            zobfs.add_edge(v, u, 1)
        else:
            zobfs.add_edge(v, u, 0)
dist = zobfs.distance(0)
ans += dist[vtx(H-1, W-1)]
print(ans)