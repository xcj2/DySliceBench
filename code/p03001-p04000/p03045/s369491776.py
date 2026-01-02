from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            if self.same_check(x, y) != True:
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[x] = y
        else:
            if self.same_check(x, y) != True:
               self.size[x] += self.size[y]
               self.size[y] = 0
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
               self.rank[x] += 1

    def siz(self, x):
        x = self.find(x)
        return self.size[x]

def getlist():
    return list(map(int, input().split()))

N, M = getlist()
U = UnionFind(N)
for i in range(M):
    X, Y, Z = getlist()
    U.union(X, Y)

D = defaultdict(int)


for i in range(1, N + 1):
    n = U.find(i)
    D[n] += 1

print(len(D))