# ABC126 E
f=lambda:map(int,input().split())
N,M=f()

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def find_root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
        
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
                
    def is_same_group(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def count(self, x):
        return -self.root[self.find_root(x)]
    
uf=UnionFind(N)
for _ in [0]*M:
    x,y,z=f()
    uf.unite(x,y)
    
res=0
for i in range(N):
    if uf.root[i+1]<0:
        res+=1
print(res)