nl = lambda: list(map(int, input().split()))
sl = lambda: input().split()
n = lambda: int(input())
s = lambda: input()


import queue
from collections import defaultdict
def max_flow(edges, num_of_vertices, start, goal):
    level = defaultdict(lambda: -1)
    seen = set()

    def bfs(s):
        level[s] = 0
        q = queue.Queue()
        q.put(s)
        while not q.empty():
            v = q.get()
            for nv, cap in edges[v].items():
                if cap > 0 and level[nv] < 0:
                    level[nv] = level[v] + 1
                    q.put(nv)

    def dfs(v, t, f):
        if v == t:
            return f
        for nv, cap in edges[v].items():
            if (v, nv) in seen:
                continue
            seen.add((v, nv))
            if cap > 0 and level[v] < level[nv]:
                d = dfs(nv, t, min(f, cap))
                if d > 0:
                    edges[v][nv] -= d
                    edges[nv][v] += d
                    return d
        return 0

    flow = 0
    while True:
        level.clear()
        bfs(start)
        if level[goal] < 0:
            return flow
        seen.clear()
        while True:
            f = dfs(start, goal, float('inf'))
            if f == 0:
                break
            flow += f
    return flow

N = n()

reds = []
edges = defaultdict(dict)

for i in range(N):
    reds.append(nl())
    edges[0][i+1] = 1
    edges[i+1][0] = 0
blues = []
for i in range(N):
    blues.append(nl())
    edges[N+i+1][2*N+1] = 1
    edges[2*N+1][N+i+1] = 0

for i in range(N):
    for j in range(N):
        rx, ry = reds[i]
        bx, by = blues[j]
        if rx < bx and ry < by:
            edges[i+1][N+j+1] = 1
            edges[N+j+1][i+1] = 0

print(max_flow(edges, 2*N+2, 0, 2*N+1))
