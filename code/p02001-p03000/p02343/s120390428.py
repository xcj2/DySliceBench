class DisjointSet:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def same(self, x, y):
        return self.find_set(x) == self.find_set(y)

    def unite(self, x, y):
        self.__link(self.find_set(x), self.find_set(y))

    def __link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_set(self.p[x])
        return self.p[x]


def main():
    n, q = map(int, input().split())
    ds = DisjointSet(n)
    for _ in range(q):
        com, x, y = map(int, input().split())
        if com == 0:
            ds.unite(x, y)
        elif com == 1:
            print(1 if ds.same(x, y) else 0)


if __name__ == '__main__':
    main()

