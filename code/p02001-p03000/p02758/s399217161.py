import sys
from bisect import bisect_left as bl
input = sys.stdin.readline
N = int(input())
mod = 998244353
rs = []
xs = []
for _ in range(N):
  x, d = map(int, input().split())
  rs.append((x, d))
  xs.append(x)
rs.sort()
xs.sort()

class SegTree:
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

seg = SegTree(N, 0, [0] * N)

for i in range(N - 1, -1, -1):
  j = bl(xs, rs[i][0] + rs[i][1])
  if j >= N: j -= 1
  else: j -= ((rs[i][0] + rs[i][1]) <= xs[j])
  seg.update(i, max(0, j, seg.query(i, j + 1)))
  #print((i, j), rs[i])

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N):
  j = seg.query(i, i + 1)
  dp[i + 1] += dp[i]
  dp[i + 1] %= mod
  dp[j + 1] += dp[i]
  dp[j + 1] %= mod
  #print(rs[i], dp)
print(dp[-1])