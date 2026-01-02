class Queue:
  def __init__(self,c):
    self.values = [None]*(c+1)
    self.s = 0
    self.t = 0

  def push(self,x):
    if self._next(self.s) == self.t:
      raise Exception("Overflow")
    self.values[self.s] = x
    self.s = self._next(self.s)

  def pop(self):
    if self.s == self.t:
      raise Exception("Underflow")
    ret = self.values[self.t]
    self.t = self._next(self.t)
    return ret

  def size(self):
    if self.s >= self.t:
      return self.s-self.t
    else:
      return len(self.values) - (self.t-self.s)


  def _next(self,p):
    p += 1
    if p >= len(self.values):
      p = 0
    return p


def solve(G):
  d = {}
  n = len(G)
  for u in G:
    d[u] = -1
  d[1] = 0
  queue = Queue(n+1)
  queue.push(1)
  while queue.size() > 0:
    u = queue.pop()
    for v in G[u]:
      if d[v] == -1:
        d[v] = d[u] + 1
        queue.push(v)
  return d







n = int(input())
G = {}
for i in range(n):
  entry = list(map(int, input().split(' ')))
  u = entry[0]
  k = entry[1]
  G[u] = set()
  for v in entry[2:]:
    G[u].add(v)


d = solve(G)
for u in G:
  print(u,d[u])