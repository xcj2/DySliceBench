import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()
from heapq import heappop, heappush

def build():
    for i in range(N - 1, 0, -1):
        cl, cr = i << 1, i << 1 | 1
        E[i].append((cl, 0))
        E[i].append((cr, 0))
        E[ref(cl + N2)].append((ref(i + N2), 0))
        E[ref(cr + N2)].append((ref(i + N2), 0))

def add_range_edge(l0, r0, l1, r1, w):
    E.append([])
    v = len(E) - 1
    _add_range_edge(l0 + N, r0 + N, v, w, to = True)
    _add_range_edge(l1 + N, r1 + N, v, 0, to = False)

def _add_range_edge(l, r, v, w, to):
    while l < r:
        if l & 1:
            E[ref(l + N2)].append((v, w)) if to else E[v].append((l, w))
            l += 1
        if r & 1:
            r -= 1
            E[ref(r + N2)].append((v, w)) if to else E[v].append((r, w))
        l >>= 1
        r >>= 1

def resolve():
    global N, N2, E, ref
    n, m = map(int, input().split())
    N = 1 << (n - 1).bit_length()
    N2, N3 = N * 2, N * 3
    E = [[] for _ in range(N3)]
    ref = lambda v : v if v < 3 * N else v - N2

    build()
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        add_range_edge(u, v, u, v, w)

    # Dijkstra (start : N, terminal : N + n - 1)
    dist = [INF] * (N3 + m)
    dist[N] = 0
    heap = [(0, N)]
    while heap:
        d, v = heappop(heap)
        if dist[v] != d:
            continue
        for nv, w in E[v]:
            if dist[nv] > d + w:
                dist[nv] = d + w
                heappush(heap, (d + w, nv))

    ans = dist[N + n - 1]
    if ans == INF:
        ans = -1
    print(ans)
resolve()