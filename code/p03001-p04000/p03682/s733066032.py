import sys
import collections
import itertools

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def grouper(self):
        import itertools
        import operator
        par = operator.itemgetter(1)
        for _, group in itertools.groupby(
                sorted(enumerate(self.par), key=par), par):
            yield [i for i, par in group]

def sliding_window(n, seq):
    import collections
    import itertools
    return zip(*(collections.deque(itertools.islice(it, i), 0) or it
               for i, it in enumerate(itertools.tee(seq, n))))

Edge = collections.namedtuple('Edge', ['s', 't', 'cost'])

N = int(sys.stdin.readline())
xys = [[i] + list(map(int, line.split())) for i, line in enumerate(sys.stdin)]
edges = []
for (i1, x1, _), (i2, x2, _) in sliding_window(2, sorted(xys, key=lambda t: t[1])):
    edges.append(Edge(i1, i2, abs(x1 - x2)))
for (i1, _, y1), (i2, _, y2) in sliding_window(2, sorted(xys, key=lambda t: t[2])):
    edges.append(Edge(i1, i2, abs(y1 - y2)))
edges = sorted(edges, key=lambda e: e.cost)
uf = UnionFind(N)
min_cost = 0
for edge in edges:
    if not uf.are_same(edge.s, edge.t):
        uf.union(edge.s, edge.t)
        min_cost += edge.cost
print(min_cost)