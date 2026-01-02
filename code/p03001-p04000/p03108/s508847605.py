from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

class UnionFind():
    def __init__(self, elements):
        self.elements = elements
        self._root = {}
        self._count= {}
        for e in self.elements:
            self._root[e] = e
            self._count[e] = 1
        
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self._root[x] = y
            self._count[y] += self._count[x]
        
    def root(self, x):
        if self._root[x] != x:
            self._root[x] = self.root(self._root[x])
        return self._root[x]
    
    def size(self, x):
        return self._count[self.root(x)]

n, m = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for j in range(m)]
A.reverse()

ans = [n * (n - 1) // 2]
uf = UnionFind(range(1, n+1))
for a, b in A:
    if uf.root(a) == uf.root(b):
        ans.append(ans[-1])
        continue
    ans.append(ans[-1] - uf.size(a) * uf.size(b))
    uf.unite(a, b)

print(*ans[:-1][::-1], sep='\n')