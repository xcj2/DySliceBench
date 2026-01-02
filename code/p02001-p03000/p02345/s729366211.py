ide = 2**31-1
def func(a,b):
  return min(a,b)
class SegmentTree:
  def __init__(self,ls,commutative = True):
    if commutative:
      self.n = len(ls)
      self.tree = [ide for i in range(self.n)]+ls
    else:
      self.n = 2**((len(ls)-1).bit_length())
      self.tree = [ide for i in range(self.n)]+ls+[ide for i in range(self.n-len(ls))]
    for i in range(1,self.n)[::-1]:
      self.tree[i] = func(self.tree[i<<1|0],self.tree[i<<1|1])
  def getall(self):
    return self.tree[1]
  def get(self,l,r):
    ret = ide
    l += self.n
    r += self.n
    while l < r:
      if l&1:
        ret = func(self.tree[l],ret)
        l += 1
      if r&1:
        ret = func(ret,self.tree[r-1])
      l >>= 1
      r >>= 1
    return ret
  def update(self,i,x):
    i += self.n
    self.tree[i] = x
    while i > 1:
      i >>= 1
      self.tree[i] = func(self.tree[i<<1|0],self.tree[i<<1|1])
import sys
input = sys.stdin.readline
n,q = map(int,input().split())
a = [2**31-1]*n
sol = SegmentTree(a,commutative=False)
for _ in range(q):
  a,b,c = map(int,input().split())
  if a == 0:
    sol.update(b,c)
  else:
    print(sol.get(b,c+1))
