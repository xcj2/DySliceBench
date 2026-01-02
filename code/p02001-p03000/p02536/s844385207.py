from sys import setrecursionlimit
setrecursionlimit(10**8)
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ

    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]

    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
    def roots(self):  # すべての根をリストで返す
        return [i for i, x in enumerate(self.parent) if i == x]

N,M = map(int,input().split())
uf = UnionFind(N+1)
for i in range(M):
    a,b = map(int,input().split())
    uf.unite(a,b)
ans = len(uf.roots())-2
print(ans)
    







    





