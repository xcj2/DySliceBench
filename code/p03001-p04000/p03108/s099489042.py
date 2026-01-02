class UnionFind:
    def __init__(self, N:int):
        """N: 大きさ"""
        self.par = [i for i in range(N)]
        self.size = [1]*N
        self.rank = [1]*N
        
    def root(self, x:int)->int:
        """根を求める"""
        if self.par[x] == x: # if root
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 経路圧縮
            return self.par[x]
        
    def is_same(self, x:int, y:int)->bool:
        """x と y が同じ集合に属するか否か"""
        return self.root(x)==self.root(y)
    
    def unite(self, x:int, y:int):
        """x と y の属する集合を併合"""
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y: return
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        elif self.rank[root_x]<self.rank[root_y]:
            root_x,root_y = root_y,root_x
        # 短いほう(y)を長いほう(x)にくっつける
        self.par[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        self.size[root_y] = 0 # もういらない
        
    def get_size(self, x:int)->int:
        """xの属するグループのサイズ"""
        return self.size[self.root(x)]
    

def main():
    N,M = map(int,input().split())
    ab = [tuple(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
    uf = UnionFind(N)
    accm = []
    for ai,bi in reversed(ab):
        if uf.is_same(ai,bi):
            accm.append(0)
        else:
            accm.append(uf.get_size(ai)*uf.get_size(bi))
        uf.unite(ai,bi)

    accm = accm[::-1]
    for i in range(1,len(accm)):
        accm[i] += accm[i-1]
    for a in accm:
        print(a)

main()