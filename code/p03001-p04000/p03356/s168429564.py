from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.d = [-1] * n

    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.d[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            if self.d[x] > self.d[y]:
                x, y = y, x
            self.d[x] += self.d[y]
            self.d[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)


    def size(self, x):
        return -self.d[self.find(x)]

n, m = map(int, input().split())
p = list(map(int, input().split()))
uf = UnionFind(n)
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    uf.unite(x, y)
ans = 0
for i in range(n):
    if uf.same(i,p[i]-1) == True:
        ans += 1
print(ans)