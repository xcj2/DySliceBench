# SegmentTree
class SegmentTree:
  def __init__(self, n, p, unit, f):
    self.num = 2**((n-1).bit_length())
    self.seg = [unit]*(2*self.num)
    for i in range(n):
      self.seg[i+self.num] = p[i]
    for i in range(self.num-1, 0, -1):
      self.seg[i] = f(self.seg[i << 1], self.seg[(i << 1)+1])
    self.f = f
    self.unit = unit

  def update(self, i, x):
    i += self.num
    self.seg[i] = x
    while i:
      i >>= 1
      self.seg[i] = self.f(self.seg[i << 1], self.seg[(i << 1)+1])

  def query(self, l, r):
    ansl = ansr = self.unit
    l += self.num
    r += self.num-1
    if l == r:
      return self.seg[l]
    while l < r:
      if l & 1:
        ansl = self.f(ansl, self.seg[l])
        l += 1
      if ~r & 1:
        ansr = self.f(self.seg[r], ansr)
        r -= 1
      l >>= 1
      r >>= 1
    if l == r:
      ansl = self.f(ansl, self.seg[l])
    return self.f(ansl, ansr)

n,k=map(int,input().split())
a=[int(input())for _ in range(n)]
m=max(a)
seg=SegmentTree(m,[0]*m,0,lambda x,y: max(x,y))
ans=0
for x in a:
  f=seg.query(max(0,x-k),min(m,x+k)+1)
  seg.update(x,f+1)
  ans=max(ans,f+1)
print(ans)