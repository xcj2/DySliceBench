import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
def check(i):
  x = []
  for j in range(N):
    if i & (1 << j):
      x.append(b[j])
    else:
      x.append(a[j])
  sx = sorted(x)
  odd = [0] * 51
  even = [0] * 51
  for j in range(N):
    odd[sx[j]] += j % 2
    even[sx[j]] += (j % 2 == 0)
  for j in range(N):
    if i & (1 << j):
      if j % 2: even[x[j]] -= 1
      else: odd[x[j]] -= 1
    else:
      if j % 2: odd[x[j]] -= 1
      else: even[x[j]] -= 1
  return min(min(odd), min(even)) >= 0
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
res = float("inf")
for i in range(pow(2, N)):
  if check(i) == False: continue
  fwk = BIT(N)
  t = 0
  odd = []
  even = []
  for j in range(N):
    if i & (1 << j):
      if j % 2: even.append((b[j], j))
      else: odd.append((b[j], j))
    else:
      if j % 2: odd.append((a[j], j))
      else: even.append((a[j], j))
  #print(t, i)
  odd.sort(key = lambda x: x[0])
  even.sort(key = lambda x: x[0])
  ind = []
  #print(t, i)
  for j in range(N):
    if j % 2: ind.append(odd[j // 2][1])
    else: ind.append(even[j // 2][1])
  #print(t, i, ind)
  for x in ind:
    t += fwk.get(x, N)
    fwk.add(x + 1, 1)
  res = min(res, t)
  #print(t, i)
if res == float("inf"): print(-1)
else: print(res)