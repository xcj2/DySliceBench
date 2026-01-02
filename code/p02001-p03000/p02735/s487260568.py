from itertools import product
from collections import deque

class ZeroOneBFS:
    def __init__(self, N):
        self.N = N
        self.E = [[] for _ in range(N)]
        
    def add_edge(self, init, end, weight, undirected=False):
        assert weight in [0, 1]
        self.E[init].append((end, weight))
        if undirected: self.E[end].append((init, weight))
        
    def distance(self, s):
        self.order = [-1] * self.N # a bfs ordering of each vertex
        self.dist = [-1] * self.N # the distance of each vertex from s
        dq = deque([(s, 0)]) # (vertex, dist)
        num = 0 # current ordering
        while dq:
            v, d = dq.popleft()
            if self.order[v] < 0: # visited v for the first time
                self.order[v] = num; self.dist[v] = d
                num += 1
                for u, w in self.E[v]:
                    if self.order[u] >= 0: continue
                    if w == 0: dq.appendleft((u, d))
                    else: dq.append((u, d+1))
        return self.order, self.dist

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
_, dist = zobfs.distance(0)
ans += dist[vtx(H-1, W-1)]
print(ans)