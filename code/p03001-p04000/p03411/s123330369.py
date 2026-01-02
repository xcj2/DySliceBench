# https://atcoder.jp/contests/arc092/submissions/13926597
# 最大流で解くという発想

# https://tjkendev.github.io/procon-library/python/max_flow/ford-fulkerson.html


# Ford-Fulkerson algorithm
class FordFulkerson:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self.G[fr].append(forward)
        self.G[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self.G[v1].append(edge1)
        self.G[v2].append(edge2)

    def dfs(self, v, t, f):
        if v == t:
            return f
        used = self.used
        used[v] = 1
        for e in self.G[v]:
            w, cap, rev = e
            if cap and not used[w]:
                d = self.dfs(w, t, min(f, cap))
                if d:
                    e[1] -= d
                    rev[1] += d
                    return d
        return 0

    def flow(self, s, t):
        flow = 0
        f = INF = 10 ** 9 + 7
        N = self.N
        while f:
            self.used = [0] * N
            f = self.dfs(s, t, INF)
            flow += f
        return flow


def main():
    N = int(input())

    reds = [tuple(map(int, input().split())) for _ in range(N)]
    blues = [tuple(map(int, input().split())) for _ in range(N)]

    ff = FordFulkerson(N * 2 + 2)
    for i, (rx, ry) in enumerate(reds, start=1):
        ff.add_edge(fr=0, to=i, cap=1)
        for j, (bx, by) in enumerate(blues, start=N + 1):
            if rx < bx and ry < by:
                ff.add_edge(fr=i, to=j, cap=1)

    for j in range(N + 1, N * 2 + 1):
        ff.add_edge(fr=j, to=N * 2 + 1, cap=1)

    ans = ff.flow(0, N * 2 + 1)
    print(ans)


if __name__ == '__main__':
    main()
