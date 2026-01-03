import heapq
from collections import defaultdict
N=int(input())
X=[]
Y=[]
dic_x=defaultdict(list)
dic_y=defaultdict(list)
for i in range(N):
  x,y=map(int,input().split())
  dic_x[x].append(i)
  dic_y[y].append(i)
  X.append(x)
  Y.append(y)
X=sorted(X)
Y=sorted(Y)
V=N
E=(V-1)*2
G=[]
for i in range(N-1):
  heapq.heappush(G,(X[i+1]-X[i],dic_x[X[i]].pop(),dic_x[X[i+1]][0]))
  heapq.heappush(G,(Y[i+1]-Y[i],dic_y[Y[i]].pop(),dic_y[Y[i+1]][0]))
 
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [e for e in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def same(self, u, v):
        return self.find_set(u) == self.find_set(v)

    def unite(self, u, v):
        u = self.find_set(u)
        v = self.find_set(v)

        if u == v:
            return

        if self.rank[u] > self.rank[v]:
            self.p[v] = u
            self.size[u] += self.size[v]
        else:
            self.p[u] = v
            self.size[v] += self.size[u]
            if self.rank[u] == self.rank[v]:
                self.rank[v] += 1

    def find_set(self, u):
        if u != self.p[u]:
            self.p[u] = self.find_set(self.p[u])

        return self.p[u]

    def update_p(self):
        for u in range(self.n):
            self.find_set(u)

    def get_size(self, u):
        return self.size[self.find_set(u)]

def Minmum_Spanning_Tree(G,V,E):
  uf=UnionFind(V)
  cnt=0
  tot_weight=0
  while cnt!=V-1:
    w,u,v=heapq.heappop(G)
    if uf.same(u-1,v-1)==False:
      uf.unite(u-1,v-1)
      tot_weight+=w
      cnt+=1
  return tot_weight

weight=Minmum_Spanning_Tree(G,V,E)
print(weight)