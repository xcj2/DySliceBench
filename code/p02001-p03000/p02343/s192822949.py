class Node:
    def __init__(self):
        self.par = self
        self.rank = 1

class Utree:
    def __init__(self, n):
        self.nodes = [Node() for i in range(n)]

    def root(self, x):
        if x.par is x:
            return x
        else:
            r = self.root(x.par)
            x.par = r
            return r

    def unite(self, x, y):
        xr = self.root(self.nodes[x])
        yr = self.root(self.nodes[y])
        if xr.rank < yr.rank:
            xr.par = yr
            yr.rank += xr.rank
        else:
            yr.par = xr
            xr.rank += yr.rank


    def same(self, x, y):
        return self.root(self.nodes[x]) is self.root(self.nodes[y])



(n, q) = map(int, input().split())
ut = Utree(n)
for i in range(q):
    (c, x, y) = map(int, input().split())
    if c==0:
        ut.unite(x, y)
    else:
        print(1 if ut.same(x, y) else 0)