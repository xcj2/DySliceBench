# -*- coding: utf-8 -*-


from collections import defaultdict

class ReRooting:
    def __init__(self, f, g, merge, ie):
        self.tree = defaultdict(list)
        self.f = f
        self.g = g
        self.merge = merge
        self.ie = ie
        self.dp = defaultdict(dict)

    def add_edge(self, u, v):
        self.tree[u].append(v)
        self.tree[v].append(u)

    def __dfs1(self, u, p):
        o = []
        s = [(u, -1)]
        while s:
            u, p = s.pop()
            o.append((u, p))
            for v in self.tree[u]:
                if v == p:
                    continue
                s.append((v, u))

        for u, p in reversed(o):
            r = self.ie
            for v in self.tree[u]:
                if v == p:
                    continue
                # ep(u_, v, self.dp)
                r = self.merge(r, self.f(self.dp[u][v], v))
            self.dp[p][u] = self.g(r, u)

    def __dfs2(self, u, p, a):
        s = [(u, p, a)]

        while s:
            u, p, a = s.pop()

            self.dp[u][p] = a

            pl = [0] * (len(self.tree[u]) + 1)
            pl[0] = self.ie
            for i, v in enumerate(self.tree[u]):
                pl[i+1] = self.merge(pl[i], self.f(self.dp[u][v], v))

            pr = [0] * (len(self.tree[u]) + 1)
            pr[-1] = self.ie
            for i, v in reversed(list(enumerate(self.tree[u]))):
                pr[i] = self.merge(pr[i+1], self.f(self.dp[u][v], v))

            for i, v in enumerate(self.tree[u]):
                if v == p:
                    continue
                r = self.merge(pl[i], pr[i+1])
                s.append((v, u, self.g(r, v)))


    def build(self, root=1):
        self.__dfs1(root, -1)
        self.__dfs2(root, -1, self.ie)

    def slv(self, u):
        r = self.ie
        for v in self.tree[u]:
            r = self.merge(r, self.f(self.dp[u][v], v))

        return r


def main():
    N, M = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N-1)]

    f = lambda x, y: x
    g = lambda x, y: x + 1
    merge = lambda x, y: (x * y) % M
    rr = ReRooting(f, g, merge, 1)
    for x, y in XY:
        rr.add_edge(x, y)

    rr.build()
    for u in range(1, N+1):
        print(rr.slv(u))



if __name__ == '__main__':
    main()
