import collections
import sys

readline = sys.stdin.buffer.readline


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    N, M, K = map(int, readline().split())
    AB = [list(map(int, readline().split())) for _ in range(M)]
    CD = [list(map(int, readline().split())) for _ in range(K)]

    E = UnionFind(N)

    ans = [0 for _ in range(N)]
    for a, b in AB:
        a -= 1
        b -= 1
        E.unite(a, b)
        ans[a] -= 1
        ans[b] -= 1

    for i in range(N):
        E.find(i)

    ll = collections.defaultdict(int)
    for i in E.par:
        ll[i] += 1

    for i in range(N):
        ans[i] += ll[E.par[i]] - 1

    for i, j in CD:
        i -= 1
        j -= 1
        if E.same(i, j):
            ans[i] -= 1
            ans[j] -= 1

    print(*ans)


main()
