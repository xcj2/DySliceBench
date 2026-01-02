# Binary Indexed Tree (Fenwick Tree)
class BIT:
  def __init__(self, n):
    self.n = n
    self.bit = [0]*(n+1)
    self.el = [0]*(n+1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.bit[i]
      i -= i & -i
    return s
  def add(self, i, x):
    # assert i > 0
    self.el[i] += x
    while i <= self.n:
      self.bit[i] += x
      i += i & -i
  def get(self, i, j=None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i-1)
  def lower_bound(self,x):
    w = i = 0
    k = 1<<((self.n).bit_length())
    while k:
      if i+k <= self.n and w + self.bit[i+k] < x:
        w += self.bit[i+k]
        i += k
      k >>= 1
    return i+1

def solve():
  N, Q = map(int, input().split())
  C = list(map(int, input().split()))
  lis = [-1]*(N+1) #各色が最後に出た位置
  bit = BIT(N) #良い玉の位置
  ans = [0]*Q
  A = [list(map(int, input().split()))+[i] for i in range(Q)]
  A.sort(key=lambda x:x[1])
  now = 0
  for l,r,ind in A:
    for i in range(now,r):
      if lis[C[i]]>=0:
        bit.add(lis[C[i]]+1,-1)
      lis[C[i]] = i
      bit.add(i+1,1)
    ans[ind] = bit.get(l,r)
    now = r
  return ans
print(*solve(),sep='\n')