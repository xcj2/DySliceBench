mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.readline
    from heapq import heappush, heappop

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

    H, W = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(input().rstrip('\n'))

    s = H*W + 1
    t = H*W + 2
    mcf = Mincostflow(H*W + 2)
    cnt = 0
    no_move = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "#":
                continue
            else:
                if grid[h][w] == "o":
                    cnt += 1
                    no_move += H + W - h - w
                    mcf.add_edge(s, h*W+w+1, 1, 0)
                if h+1 < H:
                    if grid[h+1][w] != "#":
                        mcf.add_edge(h*W+w+1, (h+1)*W+w+1, 100, 0)
                if w+1 < W:
                    if grid[h][w+1] != "#":
                        mcf.add_edge(h*W+w+1, h*W+w+2, 100, 0)
                mcf.add_edge(h*W+w+1, t, 1, H+W-h-w)
    print(no_move - mcf.flow(s, t, cnt))


if __name__ == '__main__':
    main()
