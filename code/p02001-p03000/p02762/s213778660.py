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

N,M,K = inputlist()
uf = UnionFind(N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a,b = inputlist()
    uf.union(a,b)
    graph[a].append(b)
    graph[b].append(a)
brogra = [[] for _ in range(N+1)]
li = [0]*N
for i in range(K):
    c,d = inputlist()
    if uf.same(c,d):
        brogra[c].append(d)
        brogra[d].append(c)
for i in range(1,N+1):
    li[i-1] = uf.size(i) - len(graph[i]) - len(brogra[i]) -1
print(*li)