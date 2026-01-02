import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

class RangeSpannedGraph(object):
    def __init__(self, n):
        self.n = n
        self.N = N = 1 << (n - 1).bit_length()
        N2, N3 = N * 2, N * 3
        ref = self._reflect
        E = [[] for _ in range(N3)]
        for i in range(N - 1, 0, -1):
            cl, cr = i << 1, i << 1 | 1
            E[i].append((cl, 0))
            E[i].append((cr, 0))
            E[ref(cl + N2)].append((ref(i + N2), 0))
            E[ref(cr + N2)].append((ref(i + N2), 0))
        self.E = E

    def _reflect(self, v):
        return v if v < 3 * self.N else v - 2 * self.N

    def add_range_edge(self, l0, r0, l1, r1, w):
        N, E = self.N, self.E
        E.append([])
        v = len(E) - 1
        self._add_range_edge(l0 + N, r0 + N, v, w, to = True)
        self._add_range_edge(l1 + N, r1 + N, v, 0, to = False)

    def _add_range_edge(self, l, r, v, w, to):
        E, ref, N2 = self.E, self._reflect, self.N * 2
        while l < r:
            if l & 1:
                E[ref(l + N2)].append((v, w)) if to else E[v].append((l, 0))
                l += 1
            if r & 1:
                r -= 1
                E[ref(r + N2)].append((v, w)) if to else E[v].append((r, 0))
            l >>= 1
            r >>= 1

    def to_index(self, v):
        return v + self.N

from heapq import heappop, heappush
def resolve():
    n, m = map(int, input().split())
    rsg = RangeSpannedGraph(n)
    for _ in range(m):
        u, v, w = map(int, input().split())
        u -= 1
        rsg.add_range_edge(u, v, u, v, w)

    # Dijkstra
    E = rsg.E
    dist = [INF] * len(E)
    dist[rsg.to_index(0)] = 0
    heap = [(0, rsg.to_index(0))]
    while heap:
        d, v = heappop(heap)
        if dist[v] != d:
            continue
        for nv, w in E[v]:
            if dist[nv] > d + w:
                dist[nv] = d + w
                heappush(heap, (d + w, nv))

    ans = dist[rsg.to_index(n - 1)]
    if ans == INF:
        ans = -1
    print(ans)
resolve()