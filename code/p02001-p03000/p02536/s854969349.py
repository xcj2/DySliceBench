from sys import setrecursionlimit

class UnionFind:
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def union(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.find(a), self.find(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.find(a) == self.find(b)

    def find(self, a):
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a] = self.find(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self._n
        return -self.parent_or_size[self.find(a)]

    def groups(self):
        find_buf = [self.find(i) for i in range(self._n)]
        result = [[] for _ in range(self._n)]
        for i in range(self._n): result[find_buf[i]].append(i)
        return [r for r in result if r != []]

N, M = map(int,input().split())
uf = UnionFind(N)
setrecursionlimit(10**9+7)

for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    uf.union(a,b)

print(len(uf.groups())-1)