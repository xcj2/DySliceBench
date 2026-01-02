#!/usr/bin/env python3

from pprint import pprint

INF = float('inf')

n_nodes, m_edges = map(int, input().split())
edges = []
for _ in range(m_edges):
    u, v, w = map(int, input().split())
    edges.append([u, v, w])
# pprint(edges)

edges_sorted = sorted(edges, key=lambda e: e[2])
# pprint(edges_sorted)


# Kruskal's algorithm
def find_root(v, parents):
    if v == parents[v]:
        return v
    parents[v] = find_root(parents[v], parents)
    return parents[v]


def has_same_root(u, v, parents):
    return find_root(u, parents) == find_root(v, parents)


def unite(u, v, parents):
    root_u = find_root(u, parents)
    root_v = find_root(v, parents)
    parents[root_u] = root_v
    return parents


parents = [i for i in range(n_nodes)]
res = 0
for u, v, w in edges_sorted:
    if not has_same_root(u, v, parents):
        res += w
        parents = unite(u, v, parents)
print(res)

