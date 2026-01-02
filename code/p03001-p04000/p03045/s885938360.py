class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self._size = [1] * (n+1)

    # return root of x
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self._size[x] = self._size[y] = self._size[x] + self._size[y]
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self._size[self.find(x)]


def main():
    n, m = map(int, input().split())
    u = UnionFind(n)
    for _ in range(m):
        x, y, z = map(int, input().split())
        u.unite(x, y)
    s = set()
    for i in range(1, n+1):
        s.add(u.find(i))
    print(len(s))
    
    
main()