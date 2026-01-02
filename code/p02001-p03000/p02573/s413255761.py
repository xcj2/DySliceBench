#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

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
uf = Unionfind(n)
for i in range(m):
    a,b = inm()
    uf.conn(a-1,b-1)
h = {}
x = 0
for i in range(n):
    r = uf.root(i)
    if r not in h:
        h[r] = 1
    else:
        h[r] += 1
    x = max(x,h[r])
print(x)
