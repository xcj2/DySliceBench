class UnionFind():
  def __init__(self,size):
    self.table=[-1for _ in range(size)]
  def root(self,x):
    while self.table[x]>=0:
      x=self.table[x]
    return x
  def unite(self,x,y):
    s1=self.root(x)
    s2=self.root(y)
    if s1!=s2:
      if self.table[s1]!=self.table[s2]:
        if self.table[s1]<self.table[s2]:
          self.table[s2]=s1
        else:
          self.table[s1]=s2
      else:
        self.table[s1]-=1
        self.table[s2]=s1
    return
  def same(self,x,y):
    return self.root(x)==self.root(y)
I=lambda:list(map(int,input().split()))
n,m=I()
p=I()
u=UnionFind(n)
for _ in range(m):
  a,b=I()
  u.unite(a-1,b-1)
print(sum(u.same(i,j-1)for i,j in zip(range(n),p)))