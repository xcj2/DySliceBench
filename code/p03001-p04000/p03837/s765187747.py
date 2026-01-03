from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, accumulate, combinations, combinations_with_replacement
from math import sqrt, ceil, floor, factorial, gcd
from bisect import bisect_left, bisect_right, insort_left, insort_right
from copy import deepcopy
from operator import itemgetter
from functools import reduce, lru_cache  # @lru_cache(None)
import sys  # def input(): return sys.stdin.readline().rstrip() # sys.setrecursionlimit(10**6)

from collections import defaultdict, deque
from heapq import heappush, heappop

class DiGraph:
    def __init__(self, n, edges, weight=False):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.reverse_adj = [[] for _ in range(n)]
        self.degree = [0] * n
        self.weight = defaultdict(lambda: 10**18)
        if weight:
            for u, v, weight in edges:
                self.adj[u].append(v)
                self.reverse_adj[v].append(u)
                self.degree[v] += 1
                self.weight[(u, v)] = weight
        else:
            for u, v in edges:
                self.adj[u].append(v)
                self.reverse_adj[v].append(u)
                self.degree[v] += 1
                self.weight[(u, v)] = 1

    def dijkstra(self, start, goal=None):  # O((V+E)logV)
        INF = 10**18
        dist = [INF] * self.n
        dist[start] = 0
        heap = [(0, start)]  # (dist, v)
        sp_prev = [None] * self.n  # previous node in shortest path (sp)
        while heap:
            dist_v, v = heappop(heap)
            if dist[v] < dist_v:
                continue
            for adj in self.adj[v]:
                edge_weight = self.weight[(v, adj)]
                if dist[v] + edge_weight < dist[adj]:
                    dist[adj] = dist[v] + edge_weight
                    sp_prev[adj] = v
                    heappush(heap, (dist[adj], adj))

        if goal is not None:
            if dist[goal] == INF:
                return dist, []
            else:
                path = [goal]
                v = goal
                while v != start:
                    v = sp_prev[v]
                    path.append(v)
                path.reverse()
                return dist, path
        else:
            return dist, sp_prev

    def scc_decompose(self):  # strongly connected components decomposition (強連結成分分解) O(V+E)
        used = [False] * self.n
        order = []  # 帰りがけ順
        for i in range(self.n):
            if not used[i]:
                stack = [i]
                used[i] = True
                while stack:
                    u = stack.pop()
                    u_movable = False
                    for v in self.adj[u]:  # u -> v
                        if not used[v]:
                            u_movable = True
                            used[v] = True
                            stack.append(u)
                            stack.append(v)
                            break
                    if not u_movable:
                        order.append(u)

        used = [False] * self.n
        group = [None] * self.n
        label = 0
        for v in reversed(order):
            if not used[v]:
                stack = [v]
                group[v] = label
                while stack:
                    v = stack.pop()
                    used[v] = True
                    for u in self.reverse_adj[v]:  # v -> u (reverse)
                        if not used[u]:
                            group[u] = label
                            stack.append(u)
                label += 1

        # construct reduction graph
        reduction_graph = [[] for _ in range(len(set(group)))]
        reduction_components = [[] for _ in range(len(set(group)))]
        for u in range(self.n):
            for v in self.adj[u]:  # u -> v
                if group[u] == group[v]:
                    continue
                reduction_graph[group[u]].append(group[v])
            reduction_components[group[u]].append(u)
        return reduction_graph, reduction_components, group

# ---------------------- #

def topological_sort(DAG):  # O(V+E)
    n = len(DAG)
    degree = [0] * n
    for u in range(n):
        for v in DAG[u]:  # u -> v
            degree[v] += 1
    ret = [i for i in range(n) if degree[i] == 0]
    queue = deque(ret)
    while queue:
        u = queue.popleft()
        for v in DAG[u]:
            degree[v] -= 1
            if degree[v] == 0:
                queue.append(v)
                ret.append(v)
    return ret

# ---------------------- #

n, m = (int(x) for x in input().split())
edges = []
for _ in range(m):
    a, b, c = (int(x) for x in input().split())
    a -= 1
    b -= 1
    edges.append((a, b, c))
    edges.append((b, a, c))

G = DiGraph(n, edges, weight=True)
ANS = set()
for u, v in combinations(range(n), 2):
    _, path = G.dijkstra(u, v)
    for a, b in zip(path[:], path[1:]):
        ANS.add((a, b))

ans = 0
for a, b, _ in edges:
    if (a, b) in ANS or (b, a) in ANS:
        continue
    else:
        ans += 1
print(ans//2)
