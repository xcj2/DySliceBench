def main():
    import sys
    input = sys.stdin.buffer.readline

    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.root = [-1] * (n + 1)
            self.rnk = [0] * (n + 1)

        def find_root(self, x):
            if self.root[x] < 0:
                return x
            else:
                self.root[x] = self.find_root(self.root[x])
                return self.root[x]

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

    N, M = map(int, input().split())
    X = [0] + list(map(int, input().split()))
    edge = [None] * M
    for i in range(M):
        edge[i] = tuple(map(int, input().split()))
    edge.sort(key=lambda e: e[2])

    UF = UnionFind(N+1)
    edge_num = [0] * (N+1)
    ok_num = [0] * (N+1)
    for a, b, y in edge:
        if UF.isSameGroup(a, b):
            root_a = UF.find_root(a)
            edge_num[root_a] += 1
            if X[root_a] >= y:
                ok_num[root_a] += 1
        else:
            root_a = UF.find_root(a)
            root_b = UF.find_root(b)
            UF.unite(a, b)
            root_new = UF.find_root(a)
            root_old = root_a + root_b - root_new
            X[root_new] += X[root_old]
            X[root_old] = 0
            edge_num[root_new] += edge_num[root_old] + 1
            edge_num[root_old] = 0
            ok_num[root_new] += ok_num[root_old]
            ok_num[root_old] = 0
            if X[root_new] >= y:
                ok_num[root_new] = edge_num[root_new]
                ok_num[root_old] = 0
    print(M - sum(ok_num))


if __name__ == '__main__':
    main()
