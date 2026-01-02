class Union:
  def __init__(s, num):
    s.T = [-1 for i in range(num)]
 
  def root(s, x):
    if s.T[x] < 0: return x, -s.T[x]
    t, k = s.root(s.T[x])
    s.T[x] = t
    return t, k
 
  def merge(s, x, y):
    an, am = s.root(x)
    bn, bm = s.root(y)
    if an == bn: return False
    if am < bm: an, bn  = bn, an
    s.T[an] += s.T[bn]
    s.T[bn] = an
    return True
 
  def size(s, x):
    return s.root(x)[1]

  def same(s, x, y):
    return s.root(x)[0] == s.root(y)[0]

import heapq
pop = heapq.heappop
push = heapq.heappush
q  = []

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]

uni = Union(N)

xyn = [[0] * 3 for _ in range(N)]
for i in range(N):
  x, y = xy[i]
  xyn[i] = [x, y, i]

xyn.sort()
x, y, n = xyn[0]
push(q, (y << 20) + n)
for i in range(1, N):
  x, y, n = xyn[i]
  m = pop(q)
  yy, nn = m >> 20, m % (1 << 20)
  if yy < y:
    uni.merge(nn, n)
    while q:
      p = pop(q)
      yy, nn = p >> 20, p % (1 << 20)
      if yy < y:
        uni.merge(nn, n)
      else:
        push(q, (yy << 20) + nn)
        break
  else:
    push(q, (y << 20) + n)
  push(q, m)

for i in range(N):
  print(uni.root(i)[1])
