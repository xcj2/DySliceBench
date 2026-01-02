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

n,m = inm()
a = []
b = []
for i in range(m):
    aa,bb = inm()
    a.append(aa-1)
    b.append(bb-1)
ufinit(n)
cnt = n*(n-1)//2
ngr = [1]*n
ans = [0]*m
ans[m-1] = cnt
for i in range(m-1,0,-1):
    ra = ufroot(a[i])
    rb = ufroot(b[i])
    if ra != rb:
        cnt -= ngr[ra]*ngr[rb]
        ufconn(ra,rb)
        ngr[ra] += ngr[rb]
        ngr[rb] = ngr[ra]
    ans[i-1] = cnt
for i in range(m):
    print(ans[i])
