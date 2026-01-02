# -*- coding: utf-8 -*-

# Based on the following blog.
# https://null-mn.hatenablog.com/entry/2020/04/14/124151

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
                s.append((v, u, self.g(r, u)))

    # def __dfs1(self, u, p):
    #     r = self.ie
    #     for v in self.tree[u]:
    #         if v == p:
    #             continue
    #         self.dp[u][v] = self.__dfs1(v, u)
    #         r = self.merge(r, self.f(self.dp[u][v], v))

    #     return self.g(r, u)

    # def __dfs2(self, u, p, a):
    #     for v in self.tree[u]:
    #         if v == p:
    #             self.dp[u][v] = a
    #             break
    #     pl = [0] * (len(self.tree[u]) + 1)
    #     pl[0] = self.ie
    #     for i, v in enumerate(self.tree[u]):
    #         pl[i+1] = self.merge(pl[i], self.f(self.dp[u][v], v))

    #     pr = [0] * (len(self.tree[u]) + 1)
    #     pr[-1] = self.ie
    #     for i, v in reversed(list(enumerate(self.tree[u]))):
    #         pr[i] = self.merge(pr[i+1], self.f(self.dp[u][v], v))

    #     for i, v in enumerate(self.tree[u]):
    #         if v == p:
    #             continue
    #         r = self.merge(pl[i], pr[i+1])
    #         self.__dfs2(v, u, self.g(r, v))

    def build(self, root=1):
        self.__dfs1(root, -1)
        self.__dfs2(root, -1, self.ie)

    def slv(self, u):
        r = self.ie
        for v in self.tree[u]:
            r = self.merge(r, self.f(self.dp[u][v], v))

        return self.g(r, u)


def atcoder_dp_dp_v():
    # https://atcoder.jp/contests/dp/tasks/dp_v
    # https://atcoder.jp/contests/dp/submissions/16666380
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
        print(rr.slv(u)-1)


def atcoder_abc60_f():
    # https://atcoder.jp/contests/abc160/tasks/abc160_f
    # https://atcoder.jp/contests/abc160/submissions/16666397
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]

    M = 10**9+7

    from functools import reduce

    fact = [1]
    for i in range(1, 10**6):
        fact.append(fact[-1]*i % M)

    def f(x, _):
        c = x[0]
        s = x[1]
        c *= pow(fact[s], M-2, M)
        c %= M
        return (c, s)

    def g(x, _):
        c = x[0]
        s = x[1]
        c *= fact[s]
        c %= M
        return (c, s+1)

    def merge(x, y):
        return (x[0]*y[0]%M, x[1]+y[1])

    rr = ReRooting(f, g, merge, (1, 0))
    for a, b in AB:
        rr.add_edge(a, b)

    rr.build()
    for u in range(1, N+1):
        print(rr.slv(u)[0])


def codeforces_1324_f():
    N = int(input())
    A = list(map(int, input().split()))
    UV = [list(map(int, input().split())) for _ in range(N-1)]

    f = lambda x, v: max(x, 0)

    def g(x, v):
        return x + (1 if A[v-1] == 1 else -1)

    def merge(x, y):
        return x + y

    rr = ReRooting(f, g, merge, 0)
    for u, v in UV:
        rr.add_edge(u, v)



    rr.build()
    # rr.slv(2)
    ans = []
    for u in range(1, N+1):
        ans.append(rr.slv(u))

    print(*ans)


if __name__ == '__main__':
    # atcoder_dp_dp_v()
    atcoder_abc60_f()
    # codeforces_1324_f()
