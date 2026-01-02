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

def main():
  n,m,k=LI()
  uf=UnionFind(n)

  friends=[set() for _ in range(n)]
  for _ in range(m):
    a,b=LI()
    a-=1
    b-=1
    friends[a].add(b)
    friends[b].add(a)
    uf.unite(a,b)

  blocks=[set() for _ in range(n)]
  for _ in range(k):
    a,b=LI()
    a-=1
    b-=1
    blocks[a].add(b)
    blocks[b].add(a)

  # for i in range(n):
  #   print(uf.size(i),friends[i])

  ans=[0]*n
  for i in range(n):
    par=uf.find(i)
    _ans=uf.size(i)-1-len(friends[i])
    for x in blocks[i]:
      if par==uf.find(x):
        _ans-=1

    ans[i]=_ans

  return ' '.join([str(x) for x in ans])

# main()
print(main())
