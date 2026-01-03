class UnionFind:
    def __init__(self,n):
        super().__init__()
        self.par = [-1]*n
        self.rank = [0]*n
        self.tsize = [1]*n
    
    def root(self,x):
        if self.par[x] == -1:
            return x 
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x_r = self.root(x)
        y_r = self.root(y)
        
        if self.rank[x_r]>self.rank[y_r]:
            self.par[y_r] = x_r

        elif self.rank[x_r]<self.rank[y_r]:
            self.par[x_r] = y_r

        elif x_r != y_r:
            self.par[y_r] = x_r
            self.rank[x_r] += 1

        if x_r != y_r:
            size = self.tsize[x_r]+self.tsize[y_r]
            self.tsize[x_r] = size
            self.tsize[y_r] = size

    def isSame(self,x,y):
        return self.root(x) == self.root(y)

    def size(self,x):
        return self.tsize[self.root(x)]
      
n,m = tuple(map(int,input().split()))

ll = []
uf = UnionFind(m)
for _ in range(n):
  k, *l = tuple(map(int,input().split()))
  for i in range(k-1):
    uf.unite(l[i]-1,l[i+1]-1)
  ll.append(l[0]-1)

for lang in ll:
  if not uf.isSame(lang,ll[-1]):
    print("NO")
    exit()
print("YES")
