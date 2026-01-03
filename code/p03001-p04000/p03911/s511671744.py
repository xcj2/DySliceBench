class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.height = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def getsize(self, x):
        return self.size[self.find(x)]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.height[x] < self.height[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = self.par[x]
            self.size[x] += self.size[y]
            if self.height[x] == self.height[x]:
                self.height[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
uf = UnionFind(M+1)
Lf = [None]*N
for i in range(N):
    tmp = list(map(int, input().split()))
    K, L = tmp[0], tmp[1:]
    for j in range(K-1):
        uf.unite(L[j], L[j+1])
    Lf[i] = L[0]
r = uf.find(Lf[0])
for i in range(1, N):
    if r != uf.find(Lf[i]):
        print('NO')
        exit()
print('YES')