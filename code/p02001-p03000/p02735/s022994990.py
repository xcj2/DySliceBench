from itertools import product
from collections import deque

def zero_one_bfs(E, s, init=0):
    N = len(E)
    order = [-1] * N # a bfs ordering of each vertex
    dist = [-1] * N # the distance of each vertex from s
    dq = deque([(s, init)]) # (vertex, dist)
    num = 0 # current ordering
    while dq:
        v, d = dq.popleft()
        if order[v] < 0: # visited v for the first time
            order[v] = num; dist[v] = d
            num += 1
            for u, w in E[v]:
                if order[u] >= 0: continue
                if w == 0: dq.appendleft((u, d))
                else: dq.append((u, d+1))
    return order, dist

H, W = map(int, input().split())

def vtx(i, j): return i*W + j
def coord(n): return divmod(n, W)

grid = [input() for _ in range(H)] # |string| = W
E = [[] for _ in range(H * W)]
for i, j in product(range(H), range(W)):
    v = vtx(i, j)
    check = [vtx(i+dx, j+dy) for dx, dy in [(1, 0), (0, 1)] if i+dx <= H-1 and j+dy <= W-1]
    for u in check:
        x, y = coord(u)
        if grid[i][j] == '.' and grid[x][y] == '#':
            E[v].append((u, 1))
        elif grid[i][j] == '#' and grid[x][y] == '.':
            E[v].append((u, 0))
        else:
            E[v].append((u, 0))
_, dist = zero_one_bfs(E, 0, 0 if grid[0][0] == '.' else 1)
print(dist[vtx(H-1, W-1)])