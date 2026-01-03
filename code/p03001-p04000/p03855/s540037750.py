import sys
 
sys.setrecursionlimit(10000)

N,K,L = map(int, input().split())

#print(N,K,L,D,T)

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        #self.rank = [0] * (n+1)

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        #if self.rank[x] < self.rank[y]:
        #    self.par[x] = y
        #else:
        #    self.par[y] = x
        #    if self.rank[x] == self.rank[y]:
        #        self.rank[x] += 1
        self.par[x] = y
        
    # 同じ集合に属するか判定
    #def same_check(self, x, y):
    #    return self.find(x) == self.find(y)

def execOne(num, uf):
    for _ in range(num):
        d0, d1 = map(int, input().split())
        d0 = d0 - 1
        d1 = d1 - 1
        uf.union(d0, d1)

uf_D = UnionFind(N)
uf_T = UnionFind(N)

execOne(K, uf_D)
execOne(L, uf_T)


pairs = []
for i in range(N):
    pairs.append((uf_D.find(i), uf_T.find(i)))

pairs_count = {}
for p in pairs:
    if not p in pairs_count:
        pairs_count[p] = 1
    else:
        pairs_count[p] += 1

res = [0] * N
for i in range(N):
    res[i] = pairs_count[pairs[i]]
#print(*(res[i] for i in range(N)))
print(" ".join([str(i) for i in res]))