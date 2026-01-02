from heapq import heappush, heappop

class MinimumCostFlow:
    inf = 1000000000
    def __init__(self, n):
        self.n = n
        self.edges = [[] for i in range(n)]
    def add_edge(self, f, t, cap, cost):
        self.edges[f].append([t, cap, cost, len(self.edges[t]), False])
        self.edges[t].append([f, 0, -cost, len(self.edges[f]) - 1, True]) # reverse edge
    def flow(self, s, t, flow):
        n = self.n
        g = self.edges
        inf = MinimumCostFlow.inf

        prevv = [0 for i in range(n)]
        preve = [0 for i in range(n)]
        h = [0 for i in range(n)]
        dist = [inf for i in range(n)]

        res = 0

        while flow != 0:
            dist = [inf for i in range(n)]
            dist[s] = 0
            que = [(0, s)]

            while que:
                c, v = heappop(que)
                if dist[v] < c:
                    continue
                r0 = dist[v] + h[v]
                for i, e in enumerate(g[v]):
                    w, cap, cost, _, _ = e
                    if cap > 0 and r0 + cost - h[w] < dist[w]:
                        r = r0 + cost - h[w]
                        dist[w] = r
                        prevv[w] = v
                        preve[w] = i
                        heappush(que, (r, w))

            if dist[t] == inf:
                return -1
            
            for i in range(n):
                h[i] += dist[i]

            d = flow
            v = t
            while v != s:
                d = min(d, g[prevv[v]][preve[v]][1])
                v = prevv[v]
            flow -= d
            res += d * h[t]
            v = t
            while v != s:
                e = g[prevv[v]][preve[v]]
                e[1] -= d
                g[v][e[3]][1] += d
                v = prevv[v]
        return res

import sys
readline = sys.stdin.readline
write = sys.stdout.write
N, M, F = map(int, readline().split())

mcf = MinimumCostFlow(N)
for i in range(M):
    u, v, c, d = map(int, readline().split())
    mcf.add_edge(u, v, c, d)
write("%d\n" % mcf.flow(0, N-1, F))
