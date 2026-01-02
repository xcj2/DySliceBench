import sys
input = sys.stdin.readline
N = int(input())
mod = 998244353
a = []
ys = []
for _ in range(N):
  x, y = map(int, input().split())
  a.append((x, y))
  ys.append(y)

def compress(init_val):
  t = sorted(set(init_val))
  d = dict([[t[i], i] for i in range(len(t))])
  res = [0] * len(init_val)
  for i in range(len(init_val)): res[i] = d[init_val[i]]
  return res

ys = compress(ys)
a = [(a[i][0], ys[i] + 1) for i in range(N)]
a.sort()

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

fwkl = BIT(N)
fwkr = BIT(N)
ls = [0] * N
rs = [0] * N
for i in range(N):
  ls[i] = fwkl.sum(a[i][1])
  fwkl.add(a[i][1], 1)
for i in range(N - 1, -1, -1):
  rs[i] = fwkr.sum(a[i][1])
  fwkr.add(a[i][1], 1)

table = [pow(2, i, mod) - 1 for i in range(N)]
pw = lambda x: table[x]
#print(ls, rs)
res = 0
for i in range(N):
  ld, rd = ls[i], rs[i]
  lu = i - ld
  ru = N - i - rd - 1
  for k in range(16):
    d = [0] * 4
    t = 1
    if k & 1:
      t *= pw(ld)
      t %= mod
      d[0] = 1
      d[2] = 1
    if k & 2:
      t *= pw(lu)
      t %= mod
      d[0] = 1
      d[3] = 1
    if k & 4:
      t *= pw(rd)
      t %= mod
      d[1] = 1
      d[2] = 1
    if k & 8:
      t *= pw(ru)
      t %= mod
      d[1] = 1
      d[3] = 1
    res += t * (2 ** (sum(d) == 4))
    res %= mod
print(res)