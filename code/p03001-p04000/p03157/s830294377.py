import collections
import itertools
import operator

H, W = (int(i) for i in input().split())
S = []
for i in range(H):
    S.append(input())

v = []
for i in range(H*W):
    hh = i//W
    ww = i % W
    v.append(S[hh][ww])

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

tree = UnionFind()
for i in range(H):
    for j in range(W-1):
        if S[i][j] != S[i][j+1]:
            tree.unite((i,j),(i,j+1))

for i in range(W):
    for j in range(H-1):
        if S[j][i] != S[j+1][i]:
            tree.unite((j,i),(j+1,i))

a = list(tree.grouper())
res = 0
for lis in a:
    br = 0
    wt = 0
    for po in lis:
        if S[po[0]][po[1]] == ".":
            wt += 1
        else:
            br += 1
    res += wt * br

print(res)