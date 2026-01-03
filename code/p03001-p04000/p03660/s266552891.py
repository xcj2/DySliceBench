import sys
sys.setrecursionlimit(500000)

class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]
    def find(self, x):
        """
        x が属するグループを探索
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


N = int(input())
G = [[] for _ in range(N)]
INPUT = []
for i in range(N-1):
  a,b = map(int,input().split())
  a-=1;b-=1
  G[a].append(b)
  G[b].append(a)
  INPUT.append((a,b))
visit = set([])
path = [0]
def dfs(v):
  if v in visit:
    return
  visit.add(v)
  if v == N-1:
    return
  for w in G[v]:
    if w in visit:
      continue
    path.append(w)
    dfs(w)
    if path[-1] == N-1:
      return
    path.pop()
dfs(0)
#print(path)
if len(path)%2 == 0:
  A,B = path[len(path)//2-1],path[len(path)//2]
else:
  A,B = path[len(path)//2],path[len(path)//2+1]
#print(A,B)
uf = UnionFind(N)
for i in range(N-1):
  a,b = INPUT[i]
  if (a == A and b == B) or (a == B and b == A):
    continue
  uf.union(a,b)
fen = uf.get_size(0)
snu = uf.get_size(N-1)
if fen > snu:
  print("Fennec")
else:
  print("Snuke")