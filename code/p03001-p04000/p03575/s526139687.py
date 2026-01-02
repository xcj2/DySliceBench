class UnionFind(object):
  def __init__(self,n):
    self.table=[-1]*n
 
  def find(self,x):
    parent=self.table[x]
    if parent<0:
      return x
    else:
      root=self.find(parent)
      self.table[x]=root
      return root
 
  def union(self,a,b):
    root1=self.find(a)
    root2=self.find(b)
    if root1 != root2:
      if self.table[root1] != self.table[root2]:
        if self.table[root1] < self.table[root2]:
          self.table[root2]=root1
        else:
          self.table[root1]=root2
      else:
        self.table[root1]+=(-1)
        self.table[root2]=root1
      
N,M=map(int,input().split())
B=[]
for i in range(M):
  a,b=map(int,input().split())
  B.append((a,b))

def solve(x):
  a,b=B[x]
  uf=UnionFind(N+1)
  for i in range(M):
    if i!=x:
      uf.union(B[i][0],B[i][1])
  if uf.find(a)==uf.find(b):
    return False
  else:
    return True

ans=0
for i in range(M):
  if solve(i):
    ans+=1
print(ans)
