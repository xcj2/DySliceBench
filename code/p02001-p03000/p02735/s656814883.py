from itertools import product

class BellmanFord:
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
        self.dist[s] = 0
        for _ in range(self.N):
            updated = False
            for v in range(self.N):
                d = self.dist[v]
                if d != INF:
                    for u, c in self.E[v]:
                        temp = d + c
                        if self.dist[u] > temp:
                            updated = True
                            self.dist[u] = temp
                            self.prev[u] = v
            if not updated: break # the minimum costs are already stored in dist
        else: return None # the above loop is not broken if and only if there exists a negative cycle
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
bf = BellmanFord(H * W)

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
            bf.add_edge(v, u, 1)
        else:
            bf.add_edge(v, u, 0)
dist = bf.distance(0)
ans += dist[vtx(H-1, W-1)]
print(ans)