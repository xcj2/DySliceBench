N, M = map(int, input().split())
ab = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1) # 木の高さ
        self.n = [1] * (n+1)    # グループメンバー数
        
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def find_n(self, x):
        return self.n[self.find(x)]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.n[y] = self.n[x] + self.n[y]
        else:
            self.par[y] = x
            self.n[x] = self.n[x] + self.n[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
    def is_same(self, x, y):
        return self.find(x) == self.find(y) 
def main():
    uf = UnionFind(N)
    p = N * (N - 1) // 2
    ans = [p]
    for x, y in reversed(ab):
        px = uf.find(x)
        py = uf.find(y)
        if px != py:
            #p -= uf.find_n(px) * uf.find_n(py)
            p -= uf.n[px] * uf.n[py]
            uf.unite(px, py)
        ans.append(p)
 
    for a in reversed(ans[:-1]):
        print(a)
 
 
main()
