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
k = []
l = []
for i in range(n):
    z = inl()
    k.append(z[0])
    l.append(z[1:])
ufinit(n+m)
for i in range(n):
    for j in l[i]:
        ufconn(i,j+n-1)
r = ufroot(0)
for i in range(1,n):
    if ufroot(i)!=r:
        print('NO')
        exit()
print('YES')
