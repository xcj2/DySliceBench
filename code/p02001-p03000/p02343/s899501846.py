from sys import stdin

class DisjointSet(object):
    def __init__(self, n):
        self.parent = [None] * (n+1)
        self.rank = [None] * (n+1)

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

def read_and_print_ds(n, q):
    ds = DisjointSet(n)
    for _ in range(q):
        line = [ int(i) for i in stdin.readline().strip().split() ]
        s1 = line[1]
        s2 = line[2]
        if line[0] == 0:
            ds.make_set(s1)
            ds.make_set(s2)
            ds.unite(s1, s2)
        else:
            ds.make_set(s1)
            ds.make_set(s2)
            if ds.same(s1, s2):
                print("1")
            else:
                print("0")

n, q = [ int(i) for i in input().split() ]
read_and_print_ds(n, q)
