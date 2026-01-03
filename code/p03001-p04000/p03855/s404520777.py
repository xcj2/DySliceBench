import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

N, K, L = (int(i) for i in input().split())

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

ufk = UnionFind()
for i in range(K):
    a, b = (int(i) for i in input().split())
    ufk.unite(a, b)

ufl = UnionFind()
for i in range(L):
    a, b = (int(i) for i in input().split())
    ufl.unite(a, b)

L = []
for i in range(1,N+1):
    L.append( (ufk.find(i), ufl.find(i), i) )

def countList(L, ma = None):#maは要素の個数の最大値
    if ma == None:
        ma = len(L)
    L.sort() #すでにしているなら不要
    temp = (None, None, None)
    cc = 1
    reslis = [0] * (N+1)
    v = [L[0][2]]
    for se in L:
        if temp[0] == se[0] and temp[1] == se[1]:
            cc += 1
            v.append(se[2])
        else:
            if temp[0] == None:
                pass
            else:
                for aa in v:
                    reslis[aa] = cc
                v = [se[2]]
                cc = 1
            temp = se
    for aa in v:
        reslis[aa] = cc
    return reslis

reslis = countList(L, N)
reslis = reslis[1:]
reslis = [str(i) for i in reslis]
print(" ".join(reslis))