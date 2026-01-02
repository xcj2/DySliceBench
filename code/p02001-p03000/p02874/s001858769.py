import sys
input = sys.stdin.readline
N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
for i in range(N): a[i][1] += 1
a.sort()
ls = [x[0] for x in a]
rs = [x[1] for x in a]

class SegTree:
  def segfunc(self, x, y):
    return min(x, y) #ここ判定関数（ただし結合則があるもの）
  def __init__(self, n, ide_ele, init_val):
    #####単位元######
    self.ide_ele = ide_ele
    #num:n以上の最小の2のべき乗
    self.num = 2 ** (n - 1).bit_length()
    self.seg = [self.ide_ele] * 2 * self.num
    #set_val
    for i in range(n):
      self.seg[i + self.num - 1] = init_val[i]    
    #built
    for i in range(self.num - 2, -1, -1) :
      self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2]) 
  def update(self, k, x):
    k += self.num - 1
    self.seg[k] = x
    while k + 1:
      k = (k - 1) // 2
      self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2]) 
  def query(self, p, q):
    if q <= p:
      return self.ide_ele
    p += self.num - 1
    q += self.num - 2
    res = self.ide_ele
    while q - p > 1:
      if p & 1 == 0:
        res = self.segfunc(res, self.seg[p])
      if q & 1 == 1:
        res = self.segfunc(res, self.seg[q])
        q -= 1
      p = p // 2
      q = (q - 1) // 2
    if p == q:
      res = self.segfunc(res, self.seg[p])
    else:
      res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
    return res
class Seg2ree:
  def segfunc(self, x, y):
    return max(x, y) #ここ判定関数（ただし結合則があるもの）
  def __init__(self, n, ide_ele, init_val):
    #####単位元######
    self.ide_ele = ide_ele
    #num:n以上の最小の2のべき乗
    self.num = 2 ** (n - 1).bit_length()
    self.seg = [self.ide_ele] * 2 * self.num
    #set_val
    for i in range(n):
      self.seg[i + self.num - 1] = init_val[i]    
    #built
    for i in range(self.num - 2, -1, -1) :
      self.seg[i] = self.segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2]) 
  def update(self, k, x):
    k += self.num - 1
    self.seg[k] = x
    while k + 1:
      k = (k - 1) // 2
      self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2]) 
  def query(self, p, q):
    if q <= p:
      return self.ide_ele
    p += self.num - 1
    q += self.num - 2
    res = self.ide_ele
    while q - p > 1:
      if p & 1 == 0:
        res = self.segfunc(res, self.seg[p])
      if q & 1 == 1:
        res = self.segfunc(res, self.seg[q])
        q -= 1
      p = p // 2
      q = (q - 1) // 2
    if p == q:
      res = self.segfunc(res, self.seg[p])
    else:
      res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
    return res
res = 0
segls = Seg2ree(N, 0, ls)
segrs = SegTree(N, 10 ** 10, rs)
#print(a)
for i in range(N - 1):
  l1 = segls.query(0, i)
  l2 = segls.query(i + 1, N)
  r1 = segrs.query(0, i)
  r2 = segrs.query(i + 1, N)
  if l1 == 0: l1 = 10 ** 10
  if r1 > 10 ** 9: r1 = a[i][1]
  t = a[i][1] - a[i][0] + max(0, min(r1, r2) - l2)
  t = max(t, max(0, r1 - a[i][0]) + r2 - l2)
  #print(i, t, l1, l2, r1, r2)
  res = max(res, t)
print(res)