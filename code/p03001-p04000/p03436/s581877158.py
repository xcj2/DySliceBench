import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
from collections import deque
def getN():
    return int(input())
def getList():
    return list(map(int, input().split()))
import math

h, w = getList()
INF = 1000000000

dist = [[INF for i in range(w)] for j in range(h)]
grid = []
udlr = [(0, 1), (0, -1), (-1, 0), (1, 0)]

white = 0
for i in range(h):
    state = input().strip()
    grid.append(state)
    white += state.count(".")

dist[0][0] = 1
def bfs(grid, dist):
    q = deque([])
    q.append((0, 0))
    while(q):
        a, b = q.popleft()
        # print(a, b)
        cur = dist[a][b]
        for mv in udlr:
            c, d = mv
            e, f = a + c, b + d
            if e >= 0 and e < h and f >= 0 and f < w:
                if grid[e][f] == ".":
                    if dist[e][f] > cur + 1:
                        dist[e][f] = cur + 1
                        q.append((e, f))

bfs(grid, dist)

# for g in grid:
#     print(g)
# for d in dist:
#     print(d)
if dist[h-1][w-1] == INF:
    print(-1)

else:
    print(white - dist[h-1][w-1])
