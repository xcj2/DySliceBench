N,K,L = map(int, input().split())

#print(N,K,L,D,T)

class UnionFind:
    def __init__(self, n: int) -> None:
        #マイナスならルートでその深さを表す。プラスならルートのノードを指す。
        self.nodes = [-1]*n

    def find_root(self, x: int) -> int:
        if self.nodes[x] < 0:
            return x
        else:
            self.nodes[x] = self.find_root(self.nodes[x])
            return self.nodes[x]

    def unite(self, x: int, y: int) -> None:
        x, y = self.find_root(x), self.find_root(y)
        #浅い方につなぐ
        if (x != y):
            if (x < y):
                self.nodes[y] += self.nodes[x]
                self.nodes[x] = y
            else:
                self.nodes[x] += self.nodes[y]
                self.nodes[y] = x
        
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

pairs = []
for i in range(N):
    pairs.append((uf_D.find_root(i), uf_T.find_root(i)))
 
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