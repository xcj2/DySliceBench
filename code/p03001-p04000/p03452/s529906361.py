class UnionFind():
    def __init__(self,n):
        self.n=n
        self.parents = [i for i in range(n+1)]
        self.dist = [0]*(n+1)
    def find(self,x):
        if self.parents[x]==x:
            return x
        else:
            p = self.parents[x]
            self.parents[x]=self.find(self.parents[x])
            self.dist[x] += self.dist[p]
            return self.parents[x]
    def unite(self,x,y,d):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            if self.dist[x]-self.dist[y] != d:
                print("No")
                exit()
        else:
            diff = self.dist[y]+d-self.dist[x]
            if diff>=0:
                self.parents[xRoot] = yRoot
                self.dist[xRoot] += diff
                self.find(x)
            else:
                self.parents[yRoot] = xRoot
                self.dist[yRoot] += abs(diff)
                self.find(y)
N,M = map(int,input().split())
tree = UnionFind(N)
for _ in range(M):
    L,R,D = map(int,input().split())
    tree.unite(L,R,D)
print("Yes")