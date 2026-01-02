from bisect import bisect_left
import sys
input = sys.stdin.readline

N = int(input())
XD = [[int(i) for i in input().split()] for _ in range(N)]

mod = 998244353

XD.sort()

class SegTree:
  def __init__(self, n, v, f) :
    i = 1
    while i < n : 
      i <<= 1
    self.n = i
    self.v = v
    self.f = f
    self.tree = [v] * (i << 1)

  def update(self, i, x) :
    i += self.n - 1
    self.tree[i] = x
    while i > 0 :
      i = (i - 1) // 2
      self.tree[i] = self.f(self.tree[i * 2 + 1], self.tree[i * 2 + 2])

  # [l, r)
  def query(self, l, r) :
    l = l + self.n
    r = r + self.n
    s = self.v
    while l < r :
      if r & 1 :
        r -= 1
        s = self.f(s, self.tree[r - 1])
      if l & 1 :
        s = self.f(s, self.tree[l - 1])
        l += 1
      l >>= 1
      r >>= 1
    return s

INF = 1 << 60
ST = SegTree(N, -INF, max)

xs = [x for x, _ in XD]
for i in range(N - 1, -1, -1) :
  x, d = XD[i]
  j = bisect_left(xs, x + d)
  ST.update(i, max(i, ST.query(i, j)))

dp = [0] * (N + 1)
dp[N] = 1

for i in range(N) :
  dp[i] += dp[i - 1]
  dp[i] %= mod
  j = ST.query(i, i + 1)
  dp[j] += dp[i - 1]
  dp[j] %= mod

print(dp[N-1])