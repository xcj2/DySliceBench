from collections import defaultdict
from operator import add, mul
import sys
input=sys.stdin.readline


class Reroot:
    def __init__(self, N, M):
        self.G = defaultdict(list)
        self.parents = [-1]*(N+1)
        self.dp = defaultdict(lambda: defaultdict(int))
        self.ans = [0]*(N+1)
        self.merge = lambda x,y:mul(x, y)
        self.add_root = lambda x:x#+1
        self.e = 1
        self.M = M

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
                v = self.merge(v, self.dp[s][t]+1)
            self.dp[self.parents[s]][s] = self.add_root(v)

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
                ac_l[i+1] = self.merge(ac_l[i], self.dp[s][t]+1)%self.M
            for i, t in enumerate(self.G[s][::-1]):
                ac_r[size-i-1] = self.merge(ac_r[size-i], self.dp[s][t]+1)%self.M
            self.ans[s] = self.add_root(ac_l[size])
            for i, t in enumerate(self.G[s]):
                if t == par:
                    continue
                q.append((t, self.add_root(self.merge(ac_l[i], ac_r[i+1])%self.M)))


def solve():
    N, M = map(int, input().split())
    tree = Reroot(N, M)
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree.add_edge(a, b)
        tree.add_edge(b, a)
    ans = tree.build()
    for i in range(1, N+1):
        print(ans[i])


if __name__ == "__main__":
    solve()
