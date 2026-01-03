from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.size = [1] * (n+1)
    
    # 根を検索する関数
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])
  
    # 結合(unite)する関数
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    # 同じグループに属するかを判定する関数
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
    
    # 要素が属する木の深さを返す関数
    def get_depth(self, x):
        return self.rank[self.find(x)]
    
    # 要素が属する木のサイズを返す関数
    def get_size(self, x):
        return self.size[self.find(x)]
    
    # グループ数を返す関数
    def group_sum(self):
        c = 0
        for i in range(len(self.par)):
            if self.find(i) == i:
                c += 1
        return c

if __name__ == "__main__":
    N,K,L = map(int, input().split())
    uf_r = UnionFind(N)
    uf_t = UnionFind(N)
    d = defaultdict(int)

    for i in range(K):
        p, q = [int(i) for i in input().split()]
        uf_r.unite(p, q)
    
    for i in range(L):
        r, s = [int(i) for i in input().split()]
        uf_t.unite(r, s)
    
    for i in range(1,N+1):
        d[(uf_r.find(i), uf_t.find(i))] += 1
    
    print(*[d[(uf_r.find(i), uf_t.find(i))] for i in range(1,N+1)])
    