import collections


class FordFulkerson:
    """
    Verified with http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A
    """

    def __init__(self):
        self.g = collections.defaultdict(lambda: collections.defaultdict(int))

    def add_edge(self, u, v, c):
        self.g[u][v] = c

    def dfs(self, u, t, f, used: set):
        """
        :param u: visiting node
        :param t: sink
        :param f: flow
        :param used: node u is used?
        :return: min(c, f)
        """
        if u == t:
            return f

        used.add(u)

        # visit next node
        for v, c in self.g[u].items():
            if v not in used and c > 0:
                f = min(c, f)
                d = self.dfs(v, t, f, used)

                # update the graph if a path is found
                if d > 0:
                    self.g[u][v] -= d
                    self.g[v][u] += d
                    return d

        # path is not found
        return 0

    def max_flow(self, s, t):
        """Calculate maximum flow from s to t on the network

        :param s: source
        :param t: sink
        :return: max flow on the network
        """
        f = 0
        while True:
            d = self.dfs(s, t, float("inf"), set())
            if d == 0:  # nothing to update any more
                break
            f += d
        return f


def bipartite_matching(pairs: list, X :int, Y: int):
    solver = FordFulkerson()
    s = X+Y
    t = s+1
    for x, y in pairs:
        solver.add_edge(x, X+y, 1)
    for x in range(X):
        solver.add_edge(s, x, 1)
    for y in range(Y):
        solver.add_edge(X+y, t, 1)

    return solver.max_flow(s, t)


def main():
    N = int(input())
    rs = []
    bs = []
    for i in range(N):
        x, y = map(int, input().split())
        rs.append((x, y))
    for i in range(N):
        x, y = map(int, input().split())
        bs.append((x, y))

    pairs = []
    for i in range(N):
        for j in range(N):
            r = rs[i]
            b = bs[j]
            if r[0]<b[0] and r[1]<b[1]:
                pairs.append((i, j))
    print(bipartite_matching(pairs, N, N))


if __name__ == '__main__':
    main()