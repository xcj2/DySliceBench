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
N,M = map(int,input().split())
uf = UnionFind(N)
for i in range(M):
    A,B = map(int,input().split())
    uf.unite(A-1,B-1)
minus = 0
cnt = set()
for i in range(N):
    if uf.find(i) == '-1':
        minus += 1
    else:
        cnt.add(uf.find(i))
print(len(cnt)+minus-1)

