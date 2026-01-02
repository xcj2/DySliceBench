class unionFind:
    parent = []

    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.weight = [0]*N

    def root(self, x):
        if self.parent[x] == x:
            return(x)
        else:
            p = self.root(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = p
            return(self.parent[x])

    def same(self, x, y):
        x, y = x-1, y-1
        return(self.root(x) == self.root(y))

    def unite(self, x, y, w):
        w-=self.getWeight(x)
        w+=self.getWeight(y)
        x, y = x-1, y-1
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            self.parent[x] = y
            self.weight[x] = self.weight[y]+w
            return
    def getWeight(self,x):
      x-=1
      self.root(x)
      return(self.weight[x])
N,M=map(int,input().split())
G=unionFind(N)
LRD=[tuple(map(int,input().split())) for i in range(M)]
for l,r,d in LRD:
  #print(G.parent)
  #print(G.weight)
  if G.same(l,r):
    if G.getWeight(r)-G.getWeight(l) == d:
      continue
    else:
      #print(G.parent)
      #print(G.weight)
      print("No")
      exit(0)
  else:
    G.unite(r,l,d)

print("Yes")