from collections import defaultdict

INF = 999999999999999999999

def dijkstra(G, s):
  heap = Heap()
  heap.push((s, 0))
  fixed = set()
  d = defaultdict(lambda: INF)
  d[s] = 0
  while len(heap.data) > 0:
    v = heap.pop()
    if v in fixed:
      continue
    for u in G[v]:
      if u in fixed:
        continue
      c = G[v][u]
      if d[v] + c < d[u]:
        d[u] = d[v] + c
        heap.push((u, d[u]))
    fixed.add(v)
  return d


class Heap:
  def __init__(self):
    self.data = []

  def push(self,x):
    self.data.append(x)
    i = len(self.data)-1
    while self._p(i) >= 0:
      if self.data[i][1] < self.data[self._p(i)][1]:
        tmp = self.data[i]
        self.data[i] = self.data[self._p(i)]
        self.data[self._p(i)] = tmp
        i = self._p(i)
      else:
        break

  def pop(self):
    ret = self.top()
    n = self.data.pop()
    if len(self.data) > 0:
      self.data[0] = n
      i = 0
      while True:
        if self._l(i) < len(self.data):
          l = self.data[self._l(i)]
        else:
          l = (-1, INF)
        if self._r(i) < len(self.data):
          r = self.data[self._r(i)]
        else:
          r = (-1, INF)
        if l[1] > r[1]:
          if r[1] < self.data[i][1]:
            tmp = self.data[i]
            self.data[i] = self.data[self._r(i)]
            self.data[self._r(i)] = tmp
            i = self._r(i)
          else:
            break
        else:
          if l[1] < self.data[i][1]:
            tmp = self.data[i]
            self.data[i] = self.data[self._l(i)]
            self.data[self._l(i)] = tmp
            i = self._l(i)
          else:
            break
    return ret[0]

  def top(self):
    return self.data[0]

  def _p(self, i):
    i = i+1
    return i//2-1

  def _l(self, i):
    i = i+1
    return i*2-1

  def _r(self, i):
    i = i+1
    return i*2


G = {}

n, m, r = [int(v) for v in input().strip().split(' ')]
for i in range(n):
  G[i] = {}
for _ in range(m):
  s, t, c = [int(v) for v in input().strip().split(' ')]
  G[s][t] = c

d = dijkstra(G, r)

for i in range(n):
  if d[i] == INF:
    print("INF")
  else:
    print(d[i])