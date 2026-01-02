# Acceptance of input

import sys

file_input = sys.stdin

V, E = map(int, file_input.readline().split())

adj_mat = [[0] * V for i in range(V)]

for line in file_input:
    u, v, c = map(int, line.split())
    adj_mat[u][v] = c

# Dinic's algorithm

import collections

# BFS for residual capacity network to construct level graph
def bfs(start, goal, parent):
    level = [V] * V
    unvisited = [True] * V
    queue = collections.deque()
    queue.append(start)
    level[start] = 0
    unvisited[start] = False
    while queue:
        u = queue.popleft()
        next_level = level[u] + 1
        for v, r_capacity in enumerate(adj_mat[u]):
            if (level[v] >= next_level) and (r_capacity > 0):
                level[v] = next_level
                parent[v].append(u)
                if unvisited[v]:
                    queue.append(v)
                    unvisited[v] = False
    return level[goal]

# DFS for level graph and construct blocking flow
def dfs(goal, path, parent, blocking_flow):
    v = path[-1]
    if v == goal:
        aug_path_flow = 10000
        for x, y in zip(path[1:], path[:-1]):
            aug_path_flow = min(aug_path_flow, adj_mat[x][y])
        for x, y in zip(path[1:], path[:-1]):
            adj_mat[x][y] -= aug_path_flow
            adj_mat[y][x] += aug_path_flow
        blocking_flow[0] += aug_path_flow
    else:
        for u in parent[v]:
            path.append(u)
            dfs(goal, path, parent, blocking_flow)
            path.pop()

def dinic(source, sink):
    max_flow = 0
    parent = [[] for i in range(V)]
    while bfs(source, sink, parent) != V:
        blocking_flow = [0]
        path = [sink]
        # search in reverse direction from sink
        dfs(source, path, parent, blocking_flow)
        max_flow += blocking_flow[0]
        parent = [[] for i in range(V)]
    return max_flow

# output
print(dinic(0, V - 1))