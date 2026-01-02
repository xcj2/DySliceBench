
class DisjointSet:

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [0 for i in range(n)]

    def same(self, x, y):
        return self.findset(x) == self.findset(y)

    def findset(self, x):
        if x != self.p[x]:
            self.p[x] = self.findset(self.p[x])
        return self.p[x]

    def unite(self, x, y):
        self.link(self.findset(x), self.findset(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

def main():
    n, q = map(int, input().split(' '))

    ds = DisjointSet(n)

    for _ in range(q):
        c, a, b = map(int, input().split(' '))
        
        if c == 0:
            ds.unite(a, b)
        else:
            if ds.same(a, b):
                print(1)
            else:
                print(0)


if __name__ == '__main__':
    main()

