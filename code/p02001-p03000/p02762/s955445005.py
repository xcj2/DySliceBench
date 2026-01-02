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

n,m,k = inm()
ufinit(n+1)
friend = [{} for i in range(n+1)]
for i in range(m):
    a,b = inm()
    friend[a][b] = 1
    friend[b][a] = 1
    ufconn(a,b)
blk = [{} for i in range(n+1)]
for i in range(k):
    a,b = inm()
    blk[a][b] = 1
    blk[b][a] = 1
gr = {}
for i in range(1,n+1):
    r = ufroot(i)
    if r in gr:
        gr[r] += 1
    else:
        gr[r] = 1
for i in range(1,n+1):
    r = ufroot(i)
    x = gr[r]-1
    for f in friend[i]:
        if ufroot(f)==r:
            x -= 1
    for f in blk[i]:
        if ufroot(f)==r:
            x -= 1
    printn(str(x)+' ')
print("")
