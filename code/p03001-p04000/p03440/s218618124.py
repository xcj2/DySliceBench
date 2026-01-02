class UnionFind:
    def __init__(self,n):
        self.ps = [-1]*n
    def find(self,x):
        if self.ps[x]<0:
            return x
        else:
            self.ps[x]=self.find(self.ps[x])
            return self.ps[x]
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return False
        if self.ps[x]>self.ps[y]:
            x,y = y,x
        self.ps[x] += self.ps[y]
        self.ps[y] = x
        return True
    def same(self,x,y):
        return self.find(x)==self.find(y)
    def size(self,x):
        x = self.find(x)
        return -self.ps[x]

def main():
  n,m = map(int, input().split())
  a = list(map(int, input().split()))
  uf = UnionFind(n)
  for _ in range(m):
    x,y = map(int, input().split())
    uf.unite(x,y)
  d = dict()
  res = list()
  for i in range(n):
    v = uf.find(i)
    if v not in d:
      d[v] = a[i]
    elif d[v] > a[i]:
      res.append(d[v])
      d[v] = a[i]
    else:
      res.append(a[i])
  t = len(d)
  e = (t-1)*2
  if t == 1:
    return 0
  elif len(res) < e-t:
    return 'Impossible'
  else:
    res.sort()
    return sum(x for x in d.values()) + sum(res[:e-t])
  
print(main())