import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)

class SegTree:
  def segfunc(self, x, y):
    if x[0] >= y[0]: return x
    return y
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

x = pow(2, N)
table = [0] * pow(2, N)
for i in range(pow(2, N)):
  ng = 0
  ok = x
  while ok - ng > 1:
    m = (ok + ng) // 2
    if a[i] > a[m]: ok = m
    else: ng = m
  table[i] = ok

#print(table)
seg = SegTree(x, (0, N), [(a[i], i) for i in range(x)])
tt = [0]
for i in range(N):
  t = pow(2, i)
  tt.sort(reverse = True)
  ttt = []
  for j in tt:
    #print(tt)
    if table[j] >= x:
      print("No")
      exit(0)
    y, k = seg.query(table[j], x)
    if a[j] <= y or (y == 0):
      print("No")
      exit(0)
    seg.update(k, (0, N))
    ttt.append(k)
  tt += ttt
print("Yes")