ide = 0
def func(a,b):
  return max(a,b)
class SegmentTree:
  def __init__(self,ls,commutative = True):
    if commutative == True:
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
    lret = ide
    rret = ide
    l += self.n
    r += self.n
    while l < r:
      if l&1:
        lret = func(lret,self.tree[l])
        l += 1
      if r&1:
        rret = func(self.tree[r-1],rret)
      l >>= 1
      r >>= 1
    ret = func(lret,rret)
    return ret
  def update(self,i,x):
    i += self.n
    self.tree[i] = x
    while i > 1:
      i >>= 1
      self.tree[i] = func(self.tree[i<<1|0],self.tree[i<<1|1])

n = int(input())
h = list(map(int,input().split()))
b = list(map(int,input().split()))
dp = [0 for i in range(n+1)]
ST = SegmentTree(dp)
for i in range(1,n+1):
  hi = h[i-1]
  bi = b[i-1]
  x = ST.get(0,hi)
  ST.update(hi,x+bi)
print(ST.getall())