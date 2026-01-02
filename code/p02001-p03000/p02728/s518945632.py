from collections import defaultdict
from functools import lru_cache
import sys
input=sys.stdin.readline


class Reroot:
    def __init__(self, N, e, merge, f, g):
        self.G = defaultdict(list)
        self.parents = [-1]*(N+1)
        self.dp = defaultdict(lambda: defaultdict(int))
        self.merge = merge
        self.f = f
        self.g = g
        self.e = e

    def add_edge(self, s, t):
        self.G[s].append(t)

    def build(self):
        self.dfs1(1)
        self.dfs2(1)
        return self.dp

    def dfs1(self, s):
        l = []
        q = [1]
        while q:
            s = q.pop()
            l.append(s)
            for t in self.G[s]:
                if t == self.parents[s]:
                    continue
                self.parents[t] = s
                q.append(t)

        for s in l[::-1]:
            v = self.e
            for t in self.G[s]:
                if t == self.parents[s]:
                    continue
                v = self.merge(v, self.f(self.dp[s][t], s, t))
            self.dp[self.parents[s]][s] = self.g(v, self.parents[s], s)

    def dfs2(self, s):
        q = [(s, self.e)]
        while q:
            s, dp_p = q.pop()
            par = self.parents[s]
            self.dp[s][par] = dp_p

            size = len(self.G[s])
            ac_l = [self.e] * (size+1)
            ac_r = [self.e] * (size+1)
            for i, t in enumerate(self.G[s]):
                ac_l[i+1] = self.merge(ac_l[i], self.f(self.dp[s][t], s, t))
            for i, t in enumerate(self.G[s][::-1]):
                ac_r[size-i-1] = self.merge(ac_r[size-i], self.f(self.dp[s][t], s, t))
            self.dp[-1][s] = self.g(ac_l[size], -1, s)

            for i, t in enumerate(self.G[s]):
                if t == par:
                    continue
                q.append((t, self.g(self.merge(ac_l[i], ac_r[i+1]), t, s)))


def solve():
    N = int(input())

    MOD = 10**9+7
    n = N
    fac = [1]*(n+1)
    rev = [1]*(n+1)
    d = defaultdict(list)

    for i in range(1,n+1):
        fac[i] = i*fac[i-1]%MOD
        rev[i] = pow(fac[i], MOD-2, MOD)

    merge1 = lambda x,y:x+y
    f1 = lambda x, par, s:x
    g1 = lambda x, par, s:x+1
    e1 = 0
    tree1 = Reroot(N, e1, merge1, f1, g1)

    merge2 = lambda x,y:(x*y)%MOD
    f2 = lambda x, par, s:(x*rev[tree1.dp[par][s]])%MOD
    g2 = lambda x, par, s:(x*fac[tree1.dp[par][s]-1])%MOD
    e2 = 1
    tree2 = Reroot(N, e2, merge2, f2, g2)

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree2.add_edge(a, b)
        tree2.add_edge(b, a)
        tree1.add_edge(a, b)
        tree1.add_edge(b, a)

    tree1.build()
    ans = tree2.build()

    for i in range(1, N+1):
        print(ans[-1][i])


if __name__ == "__main__":
    solve()
