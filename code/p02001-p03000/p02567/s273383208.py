import sys
input = lambda: sys.stdin.readline().rstrip()

# SegmentTree
class SegmentTree:

  def __init__(self, n, p, unit, f, g, h):
    num = 2**((n-1).bit_length())
    seg = [unit]*(num*2)
    self.lazy = [None]*(num*2)
    for i in range(n):
      seg[num+i] = p[i]
    for i in range(num-1, 0, -1):
      seg[i] = f(seg[i << 1], seg[(i << 1)+1])
    self.num = num
    self.seg = seg
    self.unit = unit
    self.flag = False
    self.f = f
    self.g = g
    self.h = h

  def gindex(self, l, r):
    l += self.num
    r += self.num
    lm = (l//(l & -l)) >> 1
    rm = (r//(r & -r)) >> 1
    mm = max(lm, rm)
    r -= 1
    while l < r:
      if r <= rm:
        yield r
      if l <= lm:
        yield l
      l >>= 1
      r >>= 1
    while l:
      if l <= mm:
        yield l
      l >>= 1

  def propagates(self, ids):
    num = self.num
    g = self.g
    h = self.h
    for i in reversed(ids):
      v = self.lazy[i]
      if v is None:
        continue
      # ここ！！！！！！！！！！！！！
      # ここ！！！！！！！！！！！！！

      newv = (v[0]//2,v[1]//2)

      # ここ！！！！！！！！！！！！！
      # ここ！！！！！！！！！！！！！
      if (i << 1) < num:
        self.lazy[i << 1] = h(self.lazy[i << 1], newv)
        self.lazy[(i << 1)+1] = h(self.lazy[(i << 1)+1], newv)
      self.seg[i << 1] = g(self.seg[i << 1], newv)
      self.seg[(i << 1)+1] = g(self.seg[(i << 1)+1], newv)
      self.lazy[i] = None

  def query(self, l, r):
    f = self.f
    if self.flag:
      *ids, = self.gindex(l, r)
      self.propagates(ids)
    ansl = ansr = self.unit
    l += self.num
    r += self.num-1
    if l == r:
      return self.seg[l]
    while l < r:
      if l & 1:
        ansl = f(ansl, self.seg[l])
        l += 1
      if r & 1 == 0:
        ansr = f(self.seg[r], ansr)
        r -= 1
      l >>= 1
      r >>= 1
    if l == r:
      ansl = f(ansl, self.seg[l])
    return f(ansl, ansr)

  def update1(self, i, x):
    i += self.num
    f = self.f
    self.seg[i] = x
    while i:
      i >>= 1
      self.seg[i] = f(self.seg[i << 1], self.seg[(i << 1)+1])

  def update2(self, l, r, x):
    self.flag = True
    *ids, = self.gindex(l, r)
    self.propagates(ids)
    num = self.num
    f = self.f
    g = self.g
    h = self.h
    l += num
    r += num-1
    if l == r:
      self.seg[l] = g(self.seg[l], x)
      for i in ids:
        self.seg[i] = f(self.seg[i << 1], self.seg[(i << 1)+1])
      return
    while l < r:
      if l & 1:
        if l < num:
          self.lazy[l] = h(self.lazy[l], x)
        self.seg[l] = g(self.seg[l], x)
        l += 1
      if r & 1 == 0:
        if r < num:
          self.lazy[r] = h(self.lazy[r], x)
        self.seg[r] = g(self.seg[r], x)
        r -= 1
      l >>= 1
      r >>= 1
      x = f(x, x)
    if l == r:
      self.lazy[l] = h(self.lazy[l], x)
      self.seg[l] = g(self.seg[l], x)
    for i in ids:
      self.seg[i] = f(self.seg[i << 1], self.seg[(i << 1)+1])
  
  def update(self, i, x):
    if type(i) is int:
      self.update1(i, x)
    else:
      self.update2(i[0], i[1], x)

n,q=map(int,input().split())
a=list(map(int,input().split()))
f=lambda x,y: max(x,y)
seg=SegmentTree(n,a,0,f,0,0)
for _ in range(q):
  t,a,b=map(int,input().split())
  if t==1:
    seg.update(a-1,b)
  if t==2:
    print(seg.query(a-1,b))
  if t==3:
    ng=a-1
    ok=n+1
    while ng+1!=ok:
      mid=(ng+ok)//2
      if seg.query(ng,mid)>=b:ok=mid
      else:ng=mid
    print(ok)