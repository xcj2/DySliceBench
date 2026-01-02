mod = 1000000007
eps = 10**-9


def main():
    import sys
    input = sys.stdin.buffer.readline

    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.root = [-1] * (n + 1)
            self.rnk = [0] * (n + 1)

        def find_root(self, x):
            while self.root[x] >= 0:
                x = self.root[x]
            return x

        def unite(self, x, y):
            x = self.find_root(x)
            y = self.find_root(y)
            if x == y:
                return
            elif self.rnk[x] > self.rnk[y]:
                self.root[x] += self.root[y]
                self.root[y] = x
            else:
                self.root[y] += self.root[x]
                self.root[x] = y
                if self.rnk[x] == self.rnk[y]:
                    self.rnk[y] += 1

        def isSameGroup(self, x, y):
            return self.find_root(x) == self.find_root(y)

        def size(self, x):
            return -self.root[self.find_root(x)]

    N, Q = map(int, input().split())
    UF = UnionFind(N)
    for _ in range(Q):
        q, u, v = map(int, input().split())
        if q == 0:
            UF.unite(u+1, v+1)
        else:
            print(int(UF.isSameGroup(u+1, v+1)))


if __name__ == '__main__':
    main()
