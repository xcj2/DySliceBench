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
a = [0] * m
b = [0] * m
for i in range(m):
    val1, val2 = map(int, input().split())
    val1 -= 1
    val2 -= 1
    a[i],b[i] = val1, val2
uf = UnionFind(n)
a.reverse()
b.reverse()
ans = [0] * m
for i in range(m):
    if uf.same(a[i], b[i]) == True:
        continue
    else:
        ans[i] = uf.size(a[i]) * uf.size(b[i])
        uf.unite(a[i], b[i])
ans.reverse()
cnt = 0
for i in range(m):
    print(ans[i] + cnt)
    cnt += ans[i]