import sys
import collections
#
# class UnionFind():
#     def __init__(self,n):
#         self.par = [i for i in range(n+1)]
#         self.rank = [0 for _ in range(n+ 1)]
#     def find(self,x):
#         if self.par[x] == x:
#             return x
#         self.par[x] = self.find(self.par[x])
#         return  self.par[x]
#
#     def same_check(self,a,b):
#             return self.find(a) == self.find(b)
#
#     def union(self,x,y):
#         if self.rank[x] > self.rank[y]:
#             self.par[y] = self.par[x]
#         else:
#             self.par[x] = self.par[y]
#             if self.rank[x] == self.rank[y]:
#                 self.rank[x] += 1

class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * (size + 1)  # 非負なら親ノード，負ならグループの要素数

    def root(self, x):  # root(x): xの根ノードを返す．
        if self.parent[x] < 0:
            return x
        elif self.parent[self.parent[x]] < 0:
            return self.parent[x]
        else:
            self.parent[x] = self.root(self.parent[x])  # xをxの根に直接つなぐ
            return self.parent[x]

    def merge(self, x, y):  # merge(x,y): xのいるグループと$y$のいるグループをまとめる
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:  # xの要素数がyの要素数より「小さい」とき入れ替える
            x, y = y, x
        self.parent[x] += self.parent[y]  # xの要素数を更新
        self.parent[y] = x  # yをxにつなぐ
        return True

    def issame(self, x, y):  # same(x,y): xとyが同じグループにあるならTrue
        return self.root(x) == self.root(y)

    def size(self, x):  # size(x): xのいるグループの要素数を返す
        return -self.parent[self.root(x)]


def do():
    sys.setrecursionlimit(100000000)

    N,K,L = list(map(int, input().split(" ")))
    querys1 = [list(map(int, input().split(" "))) for i in range(K)]
    querys2 = [list(map(int, input().split(" "))) for i in range(L)]
    uf1 = UnionFind(N + 1)
    uf2 = UnionFind(N + 1)
    for query in querys1:
        a,b= query
        uf1.merge(a,b)
    for query in querys2:
        a, b = query
        uf2.merge(a, b)
    di = collections.defaultdict(lambda :0)
    for i in range(1,N+1):
        di[ (uf1.root(i),uf2.root(i))] += 1
    anss = []
    for i in range(1,N+1):

        anss.append( str(di[(uf1.root(i),uf2.root(i))]))
    print(" ".join(anss))

if __name__ == "__main__":
    do()