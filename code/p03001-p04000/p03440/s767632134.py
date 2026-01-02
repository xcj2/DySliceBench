from collections import defaultdict

N, M = map(int, input().split())
A = [int(x) for x in input().split()]


class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


if 2 * (N - M - 1) > N:
    print('Impossible')
elif N - M == 1:
    print(0)
else:
    uf = UnionFind(N)
    for _ in range(M):
        x, y = map(int, input().split())
        uf.union(x, y)

    tree = defaultdict(list)
    for i in range(N):
        tree[uf.find(i)].append(A[i])

    ans = 0
    rest = []
    for v in tree.values():
        x = min(v)
        v.remove(x)
        rest += v
        ans += x

    rest = sorted(rest)
    ans += sum(rest[:N - M - 2])
    print(ans)
