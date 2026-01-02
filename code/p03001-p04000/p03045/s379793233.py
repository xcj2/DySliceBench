class union_find():
  def __init__(self,n):
    self.n=n
    self.parents=[-1]*n
  def find(self,x):
    if self.parents[x]<0:
      return x
    else:
      self.parents[x]=self.find(self.parents[x])
      return self.parents[x]
  def union(self,x,y):
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return 
    if self.parents[x]>self.parents[y]:
      x,y=y,x
    self.parents[x]+=self.parents[y]
    self.parents[y]=x
    
def main():
  N,M=map(int,input().split())
  box=union_find(N)
  for i in range(M):
    x,y,z=map(int,input().split())
    box.union(x-1,y-1)
  box.find(1)
  ans=0
  for i, x in enumerate(box.parents):
    if x<0:
      ans+=1
  print(ans)
main()
    
    