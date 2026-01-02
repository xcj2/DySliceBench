import collections
import itertools
import operator


class UnionFind:
    def __init__(self, x):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)
        self.size = collections.defaultdict(lambda: 1)

        if x is not None:
            for elem in range(x+1):
                _, _, _ = self.parent[elem], self.rank[elem],self.size[elem]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if not self.are_same(x,y):
            xx = self.size[x]
            yy = self.size[y]
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += xx
            else:
                self.parent[y] = x
                self.size[x] += yy
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def Size(self,x):
        return self.size[self.find(x)]

    def are_same(self, x, y):
        '''print(x,y,self.find(x),self.find(y),self.find(x) == self.find(y))'''
        return self.find(x) == self.find(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]


a,b = map(int,input().split())
c = []
uf = UnionFind(a)
for i in range(b):
    n,m = map(int,input().split())
    c.append([n,m])
co = a*(a-1)//2
ccc = []
ccc.append(co)
for i in range(b)[::-1]:
    z = uf.Size(c[i][0])
    zz = uf.Size(c[i][1])
    if not uf.are_same(c[i][0],c[i][1]):
        co -= z*zz
    if co < 0:
        co = 0
    uf.unite(c[i][0],c[i][1])
    ccc.append(co)
for i in range(b)[::-1]:
    print(ccc[i])
