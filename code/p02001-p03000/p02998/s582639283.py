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
    n = int(input())
    uf = UnionFind(n)
    potential = [[1, 1] for _ in range(n)]
    x_to_index = {}
    y_to_index = {}

    for i in range(n):
        x, y = map(int, input().split())

        # 双方にくっつけられる場合
        if x in x_to_index and y in y_to_index:
            s = uf.root(x_to_index[x])
            t = uf.root(y_to_index[y])
            xs, ys = potential[s]
            xt, yt = potential[t]
            # くっつけても意味が無い場合
            if s == t:
                uf.unite(i, s)
                potential[uf.root(i)] = [xs, ys]
            # くっつけると意味がある場合
            else:
                uf.unite(i, s)
                uf.unite(i, t)
                potential[uf.root(i)] = [xs + xt, ys + yt]
        # 片方にくっつけられる場合
        elif x in x_to_index:
            s = uf.root(x_to_index[x])
            xs, ys = potential[s]
            uf.unite(i, s)
            potential[uf.root(i)] = [xs, ys + 1]
        elif y in y_to_index:
            t = uf.root(y_to_index[y])
            xt, yt = potential[t]
            uf.unite(i, t)
            potential[uf.root(i)] = [xt + 1, yt]

        x_to_index[x] = i
        y_to_index[y] = i

    res = -n
    for v in range(n):
        if v != uf.root(v):
            continue
        x, y = potential[v]
        res += x * y

    print(res)
resolve()