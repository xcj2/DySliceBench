import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))

class BIT:
  def __init__(self, n):
    self.n = n
    self.data = [0] * (n + 1)
    self.el = [0] * (n + 1)
  def sum(self, i):
    s = 0
    while i > 0:
      s += self.data[i]
      i -= i & -i
    return s
  def add(self, i, x):
    self.el[i] += x
    while i <= self.n:
      self.data[i] += x
      i += i & -i
  def get(self, i, j = None):
    if j is None:
      return self.el[i]
    return self.sum(j) - self.sum(i)
  def lowerbound(self, s):
    x = 0
    y = 0
    for i in range(self.n.bit_length(), -1, -1):
      k = x + (1 << i)
      if k <= self.n and (y + self.data[k] < s):
        y += self.data[k]
        x += 1 << i
    return x + 1

def check(x):
  b = [0] * N
  for i in range(N):
    if a[i] <= x: b[i] = -1
    else: b[i] = 1
  cs = [0] * (N + 1)
  for i in range(N): cs[i + 1] = cs[i] + b[i]
  mn = -min(cs) + 1
  fwk = BIT(N + 1)
  k = 0
  for i in range(N + 1):
    k += fwk.sum(cs[i] + mn)
    fwk.add(cs[i] + mn, 1)
  #print(k)
  return k < N * (N + 1) // 4


ok = max(a)
ng = 0
while ok - ng > 1:
  m = (ok + ng) // 2
  if check(m): ok = m
  else: ng = m
print(ok)