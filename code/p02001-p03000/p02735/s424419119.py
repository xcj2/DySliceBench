from itertools import product
from heapq import heappush, heappop

class Dijkstra:
    def __init__(self, N):
        self.N = N # #vertices
        self.E = [[] for _ in range(N)]

    def add_edge(self, init, end, weight, undirected=False):
        self.E[init].append((end, weight))
        if undirected: self.E[end].append((init, weight))
    
    def distance(self, s):
        INF = float('inf')
        self.dist = [INF] * self.N # the distance of each vertex from s
        self.prev = [-1] * self.N # the previous vertex of each vertex on a shortest path from s
        visited = [False] * self.N
        n_visited = 0 # #(visited vertices)
        heap = []
        heappush(heap, (0, -1, s))
        while heap:
            d, p, v = heappop(heap)
            if visited[v]: continue # (s,v)-shortest path is already calculated
            self.dist[v] = d; self.prev[v] = p; visited[v] = True
            n_visited += 1
            if n_visited == self.N: break
            for u, c in self.E[v]:
                if visited[u]: continue
                temp = d + c
                if self.dist[u] > temp: heappush(heap, (temp, v, u))
        return self.dist
    
    def shortest_path(self, t):
        P = []
        prev = self.prev
        while True:
            P.append(t)
            t = prev[t]
            if t == -1: break
        return P[::-1]

H, W = map(int, input().split())
dijkstra = Dijkstra(H * W)

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
            dijkstra.add_edge(v, u, 1)
        else:
            dijkstra.add_edge(v, u, 0)
dist = dijkstra.distance(0)
ans += dist[vtx(H-1, W-1)]
print(ans)