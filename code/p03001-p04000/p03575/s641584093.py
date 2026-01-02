# coding: utf-8
# Here your code !
import sys
sys.setrecursionlimit(10**7)

def solve():
    N, M = map(int, input().split())
    edges = [[] for _ in [0] * N]
    for _ in [0] * M:
        a, b = map(int, input().split())
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)
    bridges = len(get_lowlink(edges, M)[0])
    print(bridges)
 
"""
edge_numはedgeの数
"""
def get_lowlink(edges, edge_num):

 
    n = len(edges)
    order = [-1] * n
    low = [float("inf")] * n
    bridges = []
    articulations = [0] if edge_num == n-1 and len(edges[0]) > 1 else []
    append_bridge, append_articulation = bridges.append, articulations.append
 
    def dfs(v, prev, k):
        order[v] = low[v] = k
 
        is_articulation = False
        for dest in edges[v]:
            if order[dest] == -1:
                dfs(dest, v, k + 1)
                if low[v] > low[dest]:
                    low[v] = low[dest]
                if order[v] < low[dest]:
                    append_bridge((v, dest))
                is_articulation |= order[v] <= low[dest]
 
            elif dest != prev and low[v] > order[dest]:
                low[v] = order[dest]
 
        if v > 0 and is_articulation:
            append_articulation(v)
 
    dfs(0, 0, 0)
    return bridges, articulations
 
 
if __name__ == "__main__":
    solve()