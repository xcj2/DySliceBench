mod = 1000000007
eps = 10**-9
val_max = 10**9


def main():
    import sys
    input = sys.stdin.readline
    from heapq import heappush, heappop

    # 負辺未対応
    class Mincostflow():
        def __init__(self, N):
            self.N = N
            self.adj = [[] for _ in range(N + 1)]
            self.inf = 1 << 60

        def add_edge(self, fr, to, cap, cost):
            # [to, cap, cost, rev]
            forward = [to, cap, cost, None]
            backward = forward[3] = [fr, 0, -cost, forward]
            self.adj[fr].append(forward)
            self.adj[to].append(backward)

        def flow(self, s, t, f):
            N = self.N
            adj = self.adj
            inf = self.inf

            res = 0
            H = [0] * (N + 1)
            prev_v = [0] * (N + 1)
            prev_e = [None] * (N + 1)

            dist0 = [inf] * (N + 1)
            dist = [inf] * (N + 1)

            while f:
                dist[:] = dist0
                dist[s] = 0
                pq = [(0, s)]
                while pq:
                    d, v = heappop(pq)
                    if d > dist[v]:
                        continue
                    r0 = dist[v] + H[v]
                    for e in adj[v]:
                        u, cap, cost, _ = e
                        if cap > 0 and r0 + cost - H[u] < dist[u]:
                            dist[u] = r = r0 + cost - H[u]
                            heappush(pq, (r, u))
                            prev_v[u] = v
                            prev_e[u] = e

                # flow f doesn't exist
                if dist[t] == inf:
                    return None

                for i in range(1, N + 1):
                    H[i] += dist[i]

                g = f
                v = t
                while v != s:
                    g = min(g, prev_e[v][1])
                    v = prev_v[v]
                f -= g
                res += g * H[t]
                v = t
                while v != s:
                    e = prev_e[v]
                    e[1] -= g
                    e[-1][1] += g
                    v = prev_v[v]

            return res

    N, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    s = 2*N+1
    t = 2*N+2
    mcf = Mincostflow(N*2 + 2)
    mcf.add_edge(s, t, N*K, val_max)
    for i in range(1, N+1):
        mcf.add_edge(s, i, K, 0)
        mcf.add_edge(i+N, t, K, 0)
    for i in range(1, N+1):
        for j in range(N+1, 2*N+1):
            mcf.add_edge(i, j, 1, val_max - grid[i-1][j-1-N])

    print(val_max * N * K - mcf.flow(s, t, N*K))
    ans = [["."] * N for _ in range(N)]
    for i in range(1, N+1):
        for j, cap, cost, _ in mcf.adj[i]:
            if cap == 0:
                ans[i-1][j-1-N] = "X"
    for i in range(N):
        print("".join(ans[i]))


if __name__ == '__main__':
    main()
