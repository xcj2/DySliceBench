#UnionFindクラス
class UnionFind(object):
 
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.size=[1 for i in range(n)]
 
    def find(self, x):
  
        if self.par[x] == x:
            return x
        else:
            self.par[x]=self.find(self.par[x])
            return self.par[x]
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x]+=self.size[y]
            
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def tree_size(self,x):
        return self.size[self.find(x)]
    
def main():
    n,m = map(int, input().split())
    uf = UnionFind(n)
    for i in range(m):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        if not uf.same(x,y):
            uf.union(x,y)
    res = 0
    for i in range(n):
        if uf.par[i] == i:
            res += 1
    print(res)

if __name__ == '__main__':
    main()