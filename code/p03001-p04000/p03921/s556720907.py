class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

  
n,m = (int(i) for i in input().split())
k = []
uf = UnionFind(m)
for i in range(n):
  a = []
  a = list(int(i) for i in input().split())
  a.pop(0)
  k.append(a)
for i in k:
  tmp = i[0]
 #言語ごとに同じ人がいたらunion
  for j in i[1:]:
   uf.union(tmp,j)
    
 #任意の二人が同じunionに属するか？
b = uf.find(k[0][0])
for k in k[1:]:
  if b == uf.find(k[0]):
    continue 
  else:
    print('NO')
    exit()
print('YES')