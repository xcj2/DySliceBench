import sys
sys.setrecursionlimit(10000)

def memoize(function):
    def _memoize(*args, _cache={}):
        if args in _cache:
            return _cache[args]
        result = function(*args)
        _cache[args] = result
        return result
    return _memoize


class Union_find():

    def __init__(self, num):
        self.num = num
        self.par = list(range(num))
        self.rank = [0]*num

    def find(self, x):
        px = self.par[x]
        if px == x:
            return x
        else:
            rx = self.find(px)
            self.par[x] = rx
            return rx

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] > self.rank[y]:
                self.par[y] = x
            else:
                self.par[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] = self.rank[y] + 1
        return self

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def group_num(self):
        l = set()
        for i in range(self.num):
            l.add(self.find(i))
        return len(l)


class Adjlist():

    def __init__(self, nodes, edges = None):
        self.nodes = nodes
        lis = [set() for i in range(nodes)]
        if edges is not None:
            for edge in edges:
                lis[edge[0]].add(edge[1])
        self.edges = lis

    def add_edge(self, edge):
        self.edges[edge[0]].add(edge[1])
        return self

    def discard_edge(self, edge):
        self.edges[edge[0]].discard(edge[1])
        return self

    def next_set(self, x):
        return self.edges[x]

    def include_edge(self, x, y):
        return y in self.next_set(x)

class Adjlist_weighted():

    def __init__(self, nodes, edges = None):
        self.nodes = nodes
        lis = [{} for i in range(nodes)]
        if edges is not None:
            for edge in edges:
                lis[edge[0]][edge[1]] = edge[2]
        self.edges = lis

    def add_edge(self, edge):
        self.edges[edge[0]][edge[1]] = edge[2]
        return self

    def discard_edge(self, edge):
        del self.edges[edge[0]][edge[1]]
        return self

    def next_set(self, x):
        return self.edges[x].keys()

    def include_edge(self, x, y):
        return y in self.next_set(x)

    def weight_edge(self, x, y):
        return self.edge[x][y]

class Adjmat():

    def __init__(self, nodes, edges = None):
        self.nodes = nodes
        mat = [[0]*nodes for i in range(nodes)]
        if edges is not None:
            for edge in edges:
                mat[edge[0]][edge[1]] = 1
        self.edges = mat

    def add_edge(self, edge):
        self.edges[edge[0]][edge[1]] = 1
        return self

    def discard_edge(self, edge):
        self.edges[edge[0]][edge[1]] = 0
        return self

    def include_edge(self, x, y):
        return self.edge[x][y] == 1

    def next_set(self, x):
        set = set()
        for y in range(nodes):
            if self.include_edge(x, y):
                set.add(y)
        return set


class Adjmat_weighted():

    def __init__(self, nodes, edges = None):
        self.nodes = nodes
        mat = [[None]*nodes for i in range(nodes)]
        if edges is not None:
            for edge in edges:
                mat[edge[0]][edge[1]] = edge[2]
        self.edges = mat

    def add_edge(self, edge):
        self.edges[edge[0]][edge[1]] = edge[2]
        return self

    def discard_edge(self, edge):
        self.edges[edge[0]][edge[1]] = None
        return self

    def include_edge(self, x, y):
        return self.edges[x][y] is not None

    def next_set(self, x):
        set = set()
        for y in range(nodes):
            if self.include_edge(x, y):
                set.add(y)
        return set

    def weight_edge(self, x, y):
        return self.edge[x][y]


class Graph():

    def __init__(self, nodes, adj_mat = True, weighted = False, directed = False, edges = None):
        self.nodes = nodes
        self.adj_mat = adj_mat
        self.directed = directed
        self.weighted = weighted
        if weighted:
            if not(directed):
                if edges is not None:
                    for edge in edges:
                        edges.add((edge[1], edge[0], edge[2]))
            if adj_mat:
                edges = Adjmat_weighted(nodes, edges)
            else:
                edges = Adjlist_weighted(nodes, edges)
        else:
            if not(directed):
                if edges is not None:
                    for edge in edges:
                        edges.add((edge[1], edge[0]))
            if adj_mat:
                edges = Adjmat(nodes, edges)
            else:
                edges = Adjlist(nodes, edges)
        self.edges = edges

    def add_edge(self, edge):
        self.edges.add_edge(edge)
        if not(self.directed):
            if self.weighted:
                self.edges.add_edge((edge[1], edge[0], edge[2]))
            else:
                self.edges.add_edge((edge[1], edge[0]))
        return self

    def discard_edge(self, edge):
        self.edges.discard_edge(edge)
        if not(self.directed):
            self.edges.discard_edge((edge[1], edge[0]))
        return self

    def include_edge(self, x, y):
        return self.edges.include_edge(x, y)

    def next_set(self, x):
        return self.edges.next_set(x)

    def weight_edge(self, x, y):
        if self.weighted:
            return self.edges.weight_edge(x, y)
        elif self.adj_mat:
            return self.edges[x][y]
        else:
            if self.include_edge(x, y):
                return 1
            else:
                return 0

    def union_find(self):
        uf = Union_find(self.nodes)
        if self.adj_mat:
            for i in range(self.nodes):
                for j in range(self.nodes):
                    if self.edges.include_edge(i, j):
                        uf.union(i, j)
        else:
            for i in range(self.nodes):
                for j in self.edges.next_set():
                    uf.union(i, j)
        return uf

(N, M) = tuple(map(int, input().split(" ")))
g = Graph(N, False)
for i in range(M):
    g.add_edge(tuple(map(lambda x:int(x)-1, input().split(" "))))

@memoize
def one_path(point, path=(), remin = N-1):
    if remin != 0:
        s = set(path)
        s.add(point)
        d = g.next_set(point) - s
        sum = 0
        for n in d:
            sum += one_path(n, tuple(s), remin - 1)
        return sum
    else:
        return 1

print(one_path(0))