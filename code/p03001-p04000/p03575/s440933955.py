#template
def inputlist(): return [int(j) for j in input().split()]
from collections import Counter
#template
#issueから始める
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
N,M = inputlist()
ans = 0
ab = [0]*M
for i in range(M):
    ab[i] = inputlist()
for i in range(M):
    uf = UnionFind(N)
    for j in range(M):
        if j == i:
            continue
        uf.union(ab[j][0]-1,ab[j][1]-1)
    if len(uf.roots()) != 1:
        ans +=1
print(ans)