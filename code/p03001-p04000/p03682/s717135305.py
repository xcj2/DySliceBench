class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
    def find(self, x):
        """
        x が属するグループを探索して親を出す。
        """
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y):
        """
        x と y のグループを結合
        """
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]
    def is_same(self, x, y):
        """
        x と y が同じグループか否か
        """
        return self.find(x) == self.find(y)
    def get_size(self, x):
        """
        x が属するグループの要素数
        """
        x = self.find(x)
        return self.size[x]

from heapq import heapify, heappop, heappush
N = int(input())
X = [];Y = []
for i in range(N):
  a,b = map(int,input().split())
  X.append((a,b,i))
  Y.append((a,b,i))
X.sort(key=lambda x:x[0])
Y.sort(key=lambda x:x[1])
#print(X,Y)
PQ = []
for i in range(N-1):
  difx = (X[i+1][0]-X[i][0],X[i][2],X[i+1][2])
  dify = (Y[i+1][1]-Y[i][1],Y[i][2],Y[i+1][2])
  #print(difx,dify)
  heappush(PQ,difx);heappush(PQ,dify)
uf = UnionFind(N)
ans = 0
while PQ:
  dis,a,b = heappop(PQ)
  if uf.is_same(a, b):
    continue
  ans += dis
  uf.union(a,b)
print(ans)
