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

n,m = map(int,input().split())

u = UnionFind(n)
for i in range(m):
	l = list(map(int,input().split()))
	if l[0]:
		print(int(u.are_same(l[1],l[2])))
	else:
		u.unite(l[1],l[2])




