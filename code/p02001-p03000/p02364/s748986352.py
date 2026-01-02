from sys import stdin

def read_edge(e):
    E = []
    for _ in range(e):
        line = stdin.readline().strip().split()
        u = line[0]
        v = line[1]
        w = line[2]
        E.append((int(w), int(u), int(v)))
    return E

class DisjointSet(object):
    def __init__(self, n):
        self.parent = [None] * (n + 1)
        self.rank = [None] * (n + 1)

    def make_set(self, x):
        if self.parent[x] == None:
            self.parent[x] = x
            self.rank[x] = 0

    def find_set(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        self.link(self.find_set(x), self.find_set(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def same(self, x, y):
        return self.find_set(x) == self.find_set(y)

def kuruskal(n, E):
    S = DisjointSet(n)
    for i in range(n):
        S.make_set(i)
    K = []
    for i in sorted(E):
        if S.find_set(i[1]) != S.find_set(i[2]):
            S.unite(i[1], i[2])
            K.append(i[0])

    return K

n, e = [ int(i) for i in input().split() ]
E = read_edge(e)
K = kuruskal(n, E)
print(sum(K))

