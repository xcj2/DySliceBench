import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
def LILI(n): return [LI() for _ in range(n)]
INF = 10 ** 18
MOD = 10 ** 9 + 7

'''MEMO:
1 or 2 が書かれている。
与えられた x, y, z について,
z が偶数なら A_x + A_y は偶数。つまり (1, 1) or (2, 2)
z が奇数なら上記は奇数。つまり (1, 2) or (2, 1)
最小何枚で確実にすべてわかるか。

結局 union-find して独立なグラフの個数を求める問題か。
'''

import collections
import itertools
import operator

class UnionFind:
    def __init__(self, elems=None):
        class KeyDict(dict):  # dict + キーがないときは dict[key] = key として key を返す。
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()  # キーがなければ孤立点→自身が key（parent[key]=key）
        self.rank = collections.defaultdict(int)  # 木の高さ。デフォルトでは 0。経路圧縮すると本来は rank が下がるが、その効果は無視している。
        self.size_ = collections.defaultdict(lambda: 1)  # 根に属する頂点の個数。根の値しか信用できない。

        if elems is not None:
            for elem in elems:
                _, _ = self.parent[elem], self.rank[elem]

    def find(self, x):  # あるキーの根を探す。O(α(n)). log より高速。
        if self.parent[x] == x:
            return x  # 自身が根なら自身を返す。
        else:
            self.parent[x] = self.find(self.parent[x])  # 再帰的に親を探して、すべて根に付け替える（経路圧縮）。
            return self.parent[x]

    def unite(self, x, y):  # O(α(n)). log より高速。
        x = self.find(x)  # x の根を求める。
        y = self.find(y)  # y の根を求める。
        if x == y:  # もともと同一の木なら何もしない。
            return
        if self.rank[x] < self.rank[y]:  # rank （木の高さ）の低いほうを高いほうに繋げたい。
            x, y = y, x
        self.parent[y] = x  # x の親を y にする。
        self.size_[x] += self.size_[y]
        if self.rank[x] == self.rank[y]:  # 同じ高さの木だったら片方の rank を1つ上げておく。
            self.rank[x] += 1

    def are_same(self, x, y):  # O(α(n)). log より高速。
        return self.find(x) == self.find(y)

    def size(self, x):  # O(α(n)). log より高速。
        return self.size_[self.find(x)]

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]


def main(): 
    N, M = LI()
    uf = UnionFind()
    for _ in range(M):
        X, Y, Z = LI()
        uf.unite(X, Y)
    for i in range(1, N+1):
        uf.unite(i,i)
    print(len(list(uf.grouper())))

main()