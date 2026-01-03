#Union Find
class union_find:
    #初期化
    #根なら-size,子なら親の頂点
    # par = [-1]*N
    def __init__(self, N):
        self.par = [-1]*N

    #xの根を求める
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合の併合
    def unite(self, x,y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            #sizeの大きいほうがx
            if self.par[x] > self.par[y]:
                x,y = y,x
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    #xとyが同じ集合に属するかの判定
    def same(self, x,y):
        return self.find(x) == self.find(y)

    #xが属する集合の個数
    def size(self, x):
        return -self.par[self.find(x)]

N, K, L = map(int, input().split())


uf1 = union_find(N)
for _ in range(K):
    p, q = map(int, input().split())
    p -= 1
    q -= 1
    uf1.unite(p, q)

uf2 = union_find(N)
for _ in range(L):
    r, s = map(int, input().split())
    r -= 1
    s -= 1
    uf2.unite(r, s)

pairs = [(uf1.find(i), uf2.find(i)) for i in range(N)]
from collections import Counter

cnt = Counter(pairs)
res = [cnt[pair] for pair in pairs]
print(*res)