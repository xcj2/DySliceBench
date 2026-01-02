from collections import defaultdict
import sys
input=sys.stdin.readline


class Reroot:
    def __init__(self, N, e, merge, f, g):
        self.G = defaultdict(list)
        self.parents = [-1]*(N+1)
        self.dp = defaultdict(lambda: defaultdict(int))
        self.ans = [0]*(N+1)
        self.merge = merge
        self.f = f
        self.g = g
        self.e = e

    def add_edge(self, s, t):
        self.G[s].append(t)

    def build(self):
        self.dfs1(1)
        self.dfs2(1)
        return self.ans

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
                v = self.merge(v, self.f(self.dp[s][t], 1))
            self.dp[self.parents[s]][s] = self.g(v, 0)

    def dfs2(self, s):
        q = [(s, self.e)]
        while q:
            s, dp_p = q.pop()
            par = self.parents[s]
            for t in self.G[s]:
                if t == par:
                    self.dp[s][t] = dp_p

            size = len(self.G[s])
            ac_l = [self.e] * (size+1)
            ac_r = [self.e] * (size+1)
            for i, t in enumerate(self.G[s]):
                ac_l[i+1] = self.merge(ac_l[i], self.f(self.dp[s][t], 1))
            for i, t in enumerate(self.G[s][::-1]):
                ac_r[size-i-1] = self.merge(ac_r[size-i], self.f(self.dp[s][t], 1))
            self.ans[s] = self.g(ac_l[size], 0)
            for i, t in enumerate(self.G[s]):
                if t == par:
                    continue
                q.append((t, self.g(self.merge(ac_l[i], ac_r[i+1]), 0)))


def solve():
    N, M = map(int, input().split())
    
    merge = lambda x,y:(x*y)%M
    f = lambda x,y:x+y
    g = lambda x,y:x+y
    e = 1
    tree = Reroot(N, e, merge, f, g)

    for _ in range(N-1):
        a, b = map(int, input().split())
        tree.add_edge(a, b)
        tree.add_edge(b, a)
    ans = tree.build()
    for i in range(1, N+1):
        print(ans[i])


if __name__ == "__main__":
    solve()
