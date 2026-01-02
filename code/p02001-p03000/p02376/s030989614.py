def main():
    import sys
    sys.setrecursionlimit(1000000)
    # 行先、上限、逆辺

    def add_edge(From, to, cap):
        g[From][to] = cap
        g[to][-From-1] = 0

    def max_flow(s, t):
        def dfs(v, t, f):
            q.append(v)
            if v == t:
                return f
            used[v] += 1
            for i in range(len(gkey[v])):
                to = gkey[v][i]
                cap = g[v][to]
                if to < 0:
                    to2 = -to-1
                else:
                    to2 = to
                if used[to2] or cap == 0:
                    continue
                d = dfs(to2, t, min(f, cap))
                if d > 0:
                    g[v][to] -= d
                    if to < 0:
                        to = -to-1
                    else:
                        v = -v-1
                    g[to][v] += d
                    return d
            q.pop()
            return 0

        flow = 0
        while True:
            used = [0]*n
            q = []
            f = dfs(s, t, 10**100)
            if not q:
                return flow
            flow += f

    n, m = map(int, input().split())
    g = [dict() for _ in range(n)]
    abc = [list(map(int, input().split())) for _ in [0]*m]
    for a, b, c in abc:
        add_edge(a, b, c)
    gkey = [list(i.keys()) for i in g]
    print(max_flow(0, n-1))


main()

