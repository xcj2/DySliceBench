import sys
input=sys.stdin.readline
n=int(input())
x,y=[],[]
for i in range(n):
  x_,y_=map(int,input().split())
  x.append((x_,i))
  y.append((y_,i))
x.sort()
y.sort()
edges=[]
for i in range(n-1):
  edges.append((abs(x[i][0]-x[i+1][0]),x[i][1],x[i+1][1]))
  edges.append((abs(y[i][0]-y[i+1][0]),y[i][1],y[i+1][1]))
edges.sort()
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)
def kruskal(n, edges):#edges: wでソート済み
    uf = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not uf.same(s, t):
            res+=w
            uf.union(s, t)
    return res
print(kruskal(n, edges))