from heapq import heapify, heappop, heappush

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

N,M = map(int,input().split())
A = list(map(int,input().split()))
if N == M +1:
  print(0)
  exit()
Cost = []
for i in range(N):
  heappush(Cost,[A[i],i]) #コスト、IDという順で保存。
uf = UnionFind(N)
for i in range(M):
  a,b = map(int,input().split())
  #a-=1;b-=1 #既に0index
  uf.union(a,b)
ans = 0
L = [[] for _ in range(N-M)]
dic = {}
num = 0
for i in range(N):
  par = uf.find(i)
  if par not in dic:
    dic[par] = num
    heappush(L[dic[par]],[A[i],i])
    num +=1
  else:
    heappush(L[dic[par]],[A[i],i])
#print(L)
Selected = set([])
for x in L:
  ans += x[0][0] #最小のコスト
  Selected.add(x[0][1]) #頂点
#print(Selected)
ima = N-M
while ima < 2*(N-M-1) and Cost:
  cost, ID = heappop(Cost)
  if ID in Selected:
    continue
  else:
    ans += cost
    ima += 1
if ima < 2*(N-M-1):
  print("Impossible")
else:
  print(ans)
  
