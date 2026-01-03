class UnionFind(object):

    def __init__(self, n):
        # 親のnodeを表す
        self.par = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            # 経路圧縮
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        self.par[x] = y


class UnionFindRank(UnionFind):

    def __init__(self, n):
        UnionFind.__init__(self, n)

        self.rank = [0 for _ in range(n)]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

def _abc049_d():
    """連結"""

    N, K, L = list(map(int, input().split(' ')))
    ur = UnionFindRank(N)
    for _ in range(K):
        p, q = list(map(int, input().split(' ')))
        p -= 1
        q -= 1
        ur.union(p, q)

    ut = UnionFindRank(N)
    for _ in range(L):
        r, s = list(map(int, input().split(' ')))
        r -= 1
        s -= 1
        ut.union(r, s)

    def _id(r, t):
        return r * 1e8 + t

    from collections import defaultdict
    d = defaultdict(int)

    for i in range(N):
        d[_id(ur.root(i), ut.root(i))] += 1

    for i in range(N):
        print(d[_id(ur.root(i), ut.root(i))], end=' ')

_abc049_d()