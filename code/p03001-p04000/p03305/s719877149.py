import bisect
import collections
import heapq
from collections import defaultdict
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 32


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


n, m, s, t = list(map(int, input().split()))

MAX_VAL = 10 ** 20
uvab = llmi(m)
jpy_cost = defaultdict(dict)
snuke_cost = defaultdict(dict)


def dijkstra2_scipy(adj, start, n=None, limit=None):
    """
    caution!  add 10**-10 to avoid 0 cost
    """
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph._shortest_path import dijkstra
    if limit:
        limit += 0.5
    cost, row_ind, col_ind = [], [], []
    for k1, _v in adj.items():
        for k2, _cost in _v.items():
            row_ind.append(k1)
            col_ind.append(k2)
            cost.append(_cost + 10 ** -10)
    cost_matrix = csr_matrix((cost, (row_ind, col_ind)))
    return dijkstra(cost_matrix, indices=[start])[0]


def dijkstra2(adj, start, n):
    MAX_VAL = float('inf')
    INF = MAX_VAL
    dist = [INF for _ in range(n)]
    dist[start] = 0
    pq = []
    heapq.heappush(pq, [dist[start], start])
    while pq:
        u_dist, u_id = heapq.heappop(pq)  # u is a tuple [u_dist, u_id]
        if u_dist == dist[u_id]:
            for v in adj[u_id]:
                w_uv = adj[u_id][v]
                if dist[u_id] + w_uv < dist[v]:
                    dist[v] = dist[u_id] + w_uv
                    heapq.heappush(pq, [dist[v], v])
    return dist


for u, v, a, b in uvab:
    u = u - 1
    v = v - 1
    jpy_cost[u][v] = a
    jpy_cost[v][u] = a
    snuke_cost[u][v] = b
    snuke_cost[v][u] = b

jpy_dijk = dijkstra2(jpy_cost, start=s - 1, n=n)
snuke_dijk = dijkstra2(snuke_cost, start=t - 1, n=n)
res = []
min_val = MAX_VAL
for i in reversed(range(n)):
    # 都市  i で両替
    val = jpy_dijk[i] + snuke_dijk[i]
    assert val < MAX_VAL
    min_val = min(min_val, val)
    res.append(min_val)
for x in reversed(res):
    print(10 ** 15 - int(x))
