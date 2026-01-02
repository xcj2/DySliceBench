from itertools import combinations
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
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
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    def Count(self, x):
        return -self.root[self.Find_Root(x)]

n,m=map(int,input().split())
uf=UnionFind(n)
e=[]
comb=list(combinations(list(range(n)),2))
for _ in range(m):
  a,b=map(int,input().split())
  e.append((a-1,b-1))
ans=0
for i in range(m):
  uf=UnionFind(n)
  for j in range(m):
    if i==j:continue
    uf.Unite(*e[j])
  if not all([uf.isSameGroup(x,y) for x,y in comb]):ans+=1
print(ans)