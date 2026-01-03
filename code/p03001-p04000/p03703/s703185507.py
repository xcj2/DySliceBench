import sys
input = sys.stdin.readline
N, K = map(int, input().split())
a = [0] * N
for i in range(N): a[i] = int(input())
cs = [0] * (N + 1)
for i in range(N): cs[i + 1] = cs[i] + a[i]
#print(cs)
table = [0] * (N + 1)
for i in range(1, N + 1): table[i] = cs[i] - i * K
#print(table)
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

fwk = BIT(N + 1)

def compress(init_val):
  t = sorted(set(init_val))
  d = dict([[t[i], i] for i in range(len(t))])
  res = [0] * len(init_val)
  for i in range(len(init_val)): res[i] = d[init_val[i]]
  return res

comtable = compress(table)

for i in range(N + 1): fwk.add(comtable[i] + 1, 1)

res = 0
for i in range(N):
  fwk.add(comtable[i] + 1, -1)
  res += fwk.get(comtable[i], N + 1)
print(res)