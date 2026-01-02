import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7


import collections
import itertools
import operator


class UnionFind:
    def __init__(self, elems=None):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)

        if elems is not None:
            for elem in elems:
                _, _ = self.parent[elem], self.rank[elem]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]


def main(): 
    N = II()
    position = []
    for _ in range(N):
        position.append(LI())

    min_ = INF
    import itertools
    for A, B in itertools.combinations(range(N), 2):
        uf = UnionFind(range(N))
        p = position[A][0] - position[B][0]
        q = position[A][1] - position[B][1]
        # print(p,q)
        uf.unite(A, B)
        for X, Y in itertools.combinations(range(N), 2):
            if A == X and B == Y:
                continue
            if (p == position[X][0] - position[Y][0] and q == position[X][1] - position[Y][1]) or (p == position[Y][0] - position[X][0] and q == position[Y][1] - position[X][1]):
                uf.unite(X, Y)
        
        min_ = min(min_, len(list(uf.grouper())))
    print(1 if N == 1 else min_)

main()