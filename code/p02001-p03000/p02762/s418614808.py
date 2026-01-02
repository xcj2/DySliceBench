import sys
input=sys.stdin.readline
class UnionFind():
  def __init__(self,n):
    self.n=n
    self.parent=list(range(n))
    self.size=[1]*n
    #print(self.size, end=" self.size \n")
  def find(self,x):
    if self.parent[x]==x:
      return x
    else:
      self.parent[x]=self.find(self.parent[x])
      return self.parent[x]
  def union(self,x,y):
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return
    else:
      if self.size[x]>=self.size[y]:
        self.parent[y]=x
        self.size[x]+=self.size[y]
      else:
        self.parent[x]=y
        self.size[y]+=self.size[x]
  def cnt(self,x):
    return self.size[self.find(x)]
def main():
  n,m,k=map(int,input().split())
  u=UnionFind(n)
  ans=[0]*n
  for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    u.union(a,b)
    ans[a]-=1
    ans[b]-=1
  for _ in range(k):
    c,d=map(int,input().split())
    c-=1
    d-=1
    if u.find(c)==u.find(d):
      ans[c]-=1
      ans[d]-=1
  for i in range(n):
    ans[i]+=u.cnt(i)-1
  print(" ".join(map(str,ans)))
main()
