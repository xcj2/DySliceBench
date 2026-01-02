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


'''
独立なグラフがいくつかできていく。
求めるもの：グラフ1にある頂点と2にある頂点の combinaton, 1と3のcombination,……2と3のcombination…… の総和を求めるのを繰り返す。
union-findで行けそうだがN, Mどちらも10**5なので間に合わなさそう。

最終的にはすべて独立となり、答えはnC2となる。
ということで nC2 からはじめてどんどん union していけばいいのでは。
union する2つのグループの頂点数の積を引いていけば良いのかな。
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

    def find(self, x):  # あるキーの根を探す。
        if self.parent[x] == x:
            return x  # 自身が根なら自身を返す。
        else:
            self.parent[x] = self.find(self.parent[x])  # 再帰的に親を探して、すべて根に付け替える（経路圧縮）。
            return self.parent[x]

    def unite(self, x, y):
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

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self.size_[self.find(x)]

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]


def main(): 
    N, M = LI()

    visited = [False]*(N+1)
    uf = UnionFind()

    ans_rev = [0]*(M+1)
    ans_rev[0] = N * (N-1) // 2  # N_C_2
    A_li, B_li = [], []
    for i in range(0, M):
        A, B = LI()
        A_li.append(A)
        B_li.append(B)

    for i, (A, B) in enumerate(reversed(list(zip(A_li, B_li)))):
        if not uf.are_same(A, B):
            ans_rev[i+1] = ans_rev[i] - uf.size(A) * uf.size(B)
        else:
            ans_rev[i+1] = ans_rev[i]
        uf.unite(A, B)

    for i in reversed(ans_rev[:-1]):
        print(i)


main()