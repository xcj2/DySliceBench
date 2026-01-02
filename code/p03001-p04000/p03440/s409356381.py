printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

# # # # unionfind.py # # # #

# usage: uf = Unionfind(n) ; x = uf.root(y); uf.conn(a,b)

class Unionfind:

  def __init__(s,n):
    s.sz = [1] * n
    s.ances = [i for i in range(n)]

  def root(s,x):
    a = []
    y = x
    while s.ances[y] != y:
      a.append(y)
      y = s.ances[y]
    for z in a:
      s.ances[z] = y
    return y

  def conn(s,x,y):
    i = s.root(x)
    j = s.root(y)
    if i==j:
      return
    #k  = [i,j].min
    k  = j if (s.sz[i]<s.sz[j]) else i
    if k==j:
      s.ances[i] = j
    else:
      s.ances[j] = i
    s.sz[k] = s.sz[i] + s.sz[j]

# # # # end unionfind.py # # # #

n,m = inm()
a = inl()
nouse = 2*m-n+2
if n-m==1:
    print('0')
    exit()
if nouse<0:
    print('Impossible')
    exit()
uf = Unionfind(n)
for i in range(m):
    x,y = inm()
    uf.conn(x,y)
g = {}
for i in range(n):
    r = uf.root(i)
    if r not in g:
        g[r] = []
    g[r].append((a[i],i))

import heapq
h = []
for r in g:
    if len(g[r])<=1:
        continue
    g[r].sort()
    x,i = g[r].pop()
    heapq.heappush(h,(-x,r))
sm = 0
for i in range(nouse):
    xm,r = heapq.heappop(h)
    sm -= xm
    if len(g[r])>1:
        y,j = g[r].pop()
        heapq.heappush(h,(-y,r))
print(sum(a)-sm)
