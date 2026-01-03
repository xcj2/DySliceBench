N,K,L = map(int, input().split())

#print(N,K,L,D,T)

class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x: int, y: int) -> None:
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        
    # 同じ集合に属するか判定
    #def same_check(self, x, y):
    #    return self.find(x) == self.find(y)

def uniteOne(num, uf):
    for _ in range(num):
        d0, d1 = map(int, input().split())
        uf.unite(d0-1, d1-1)
        
uf_D = UnionFind(N)
uf_T = UnionFind(N)

uniteOne(K, uf_D)
uniteOne(L, uf_T)

from collections import Counter

keys = []
counts = Counter()

for i in range(N):
    key = uf_D.find(i), uf_T.find(i)
    keys.append(key)
    counts[key] += 1

print(*(counts[key] for key in keys))