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

def main():

    n= int(input())
    edge = []
    for i in range(n):
      x,y = list(map(int,input().split()))
      edge.append((x,y,i))
    
    xs = sorted(edge,key=lambda a:a[0])
    ys = sorted(edge,key=lambda a:a[1])

    edge = []
    
    for i in range(n-1):
      x1,y1,p1 = xs[i]
      x2,y2,p2 = xs[i+1]
      edge.append((p1,p2,min(x2-x1,abs(y2-y1))))
      
      x1,y1,p1 = ys[i]
      x2,y2,p2 = ys[i+1]
      edge.append((p1,p2,min(abs(x2-x1),y2-y1)))
    edge.sort(key = lambda a:a[2])  
    uf = UnionFind(n)
    
    ans = 0
    for x,y,w in edge:
      if uf.isSame(x,y):continue
      uf.unite(x,y)
      ans+=w
    print(ans)
      
if __name__ == "__main__":
    main()
