from sys import stdout
printn = lambda x: stdout.write(str(x))
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 999999999
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

n = inn()
x = []
y = []
for i in range(n):
    xx,yy = inm()
    x.append((xx,i))
    y.append((yy,i))
x.sort()
y.sort()
dx = []
dy = []
for i in range(n-1):
    dx.append((abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]))
    dy.append((abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]))
dx.sort(reverse=True)
dy.sort(reverse=True)
ufinit(n)
dxt = dx.pop()
dyt = dy.pop()
sm = 0
while dxt and dyt:
    #print(dxt)
    #print(dyt)
    if dxt[0]<dyt[0]:
        if ufroot(dxt[1])!=ufroot(dxt[2]):
            sm += dxt[0]
            ufconn(dxt[1],dxt[2])
        dxt = False if len(dx)==0 else dx.pop()
    else:
        if ufroot(dyt[1])!=ufroot(dyt[2]):
            sm += dyt[0]
            ufconn(dyt[1],dyt[2])
        dyt = False if len(dy)==0 else dy.pop()
print(sm)
