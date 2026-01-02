import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Union-Find -- START --
class UnionFind():
  def __init__(self,sz):
    self.sz=sz
    self.data=[-1]*sz

  def unite(self,x,y):
    x=self.find(x)
    y=self.find(y)
    if x==y:
      return False
    if self.data[x]>self.data[y]:
      x,y=y,x
    self.data[x]+=self.data[y]
    self.data[y]=x
    return True

  def find(self,k):
    if self.data[k]<0:
      return k
    self.data[k]=self.find(self.data[k])
    return self.data[k]

  def size(self,k):
    return -self.data[self.find(k)]
# Union-Find --- END ---

def main():
  n,m=LI()
  uf=UnionFind(n)
  for _ in range(m):
    a,b,c=LI()
    a-=1
    b-=1
    uf.unite(a,b)

  checked=[False]*n
  ans=0
  for i in range(n):
    a=uf.find(i)
    if checked[a]==False:
      checked[a]=True
      ans+=1

  return ans

# main()
print(main())
