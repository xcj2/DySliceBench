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

def ufinit(n):
  global ufsz, ufances
  ufsz = [1] * n
  ufances = [0] * n
  for i in range(n):
    ufances[i] = i

def ufroot(x):
  global ufances
  a = []
  y = x
  while ufances[y] != y:
    a.append(y)
    y = ufances[y]
  for z in a:
    ufances[z] = y
  return y

def ufconn(x,y):
  global ufsz, ufances
  i = ufroot(x)
  j = ufroot(y)
  if i==j:
    return
  #k  = [i,j].min
  k  = j if (ufsz[i]<ufsz[j]) else i
  if k==j:
    ufances[i] = j
  else:
    ufances[j] = i
  ufsz[k] = ufsz[i] + ufsz[j]


n,m = inm()
p = inl()
p[0:0] = [0]
x = []
y = []
for i in range(m):
    xx,yy = inm()
    x.append(xx)
    y.append(yy)
ufinit(n+1)
for i in range(m):
    ufconn(x[i],y[i])
ga = [0]*(n+1)
gb = [0]*(n+1)
for i in range(1,n+1):
    r = ufroot(i)
    ga[i] = gb[p[i]] = r
sm = 0
for i in range(1,n+1):
    if ga[i]==gb[i]:
        sm += 1
print(sm)
