import sys
INF = 1 << 60
MOD = 10**9 + 7 # 998244353
sys.setrecursionlimit(2147483647)
input = lambda:sys.stdin.readline().rstrip()

class UnionFind(object):
    def __init__(self, n, recursion = False):
        self._par = list(range(n))
        self._size = [1] * n
        self._recursion = recursion

    def root(self, k):
        if self._recursion:
            if k == self._par[k]:
                return k
            self._par[k] = self.root(self._par[k])
            return self._par[k]
        else:
            root = k
            while root != self._par[root]: root = self._par[root]
            while k != root: k, self._par[k] = self._par[k], root
            return root

    def unite(self, i, j):
        i, j = self.root(i), self.root(j)
        if i == j: return False
        if self._size[i] < self._size[j]: i, j = j, i
        self._par[j] = i
        self._size[i] += self._size[j]
        return True

    def is_connected(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, k):
        return self._size[self.root(k)]

def resolve():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        uf.unite(u, v)

    ans = len(set(uf.root(v) for v in range(n))) - 1
    print(ans)
resolve()