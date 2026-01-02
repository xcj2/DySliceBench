from sys import stdout
printn = lambda x: stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split()) 
DBG = True # and False
BIG = 999999999
R = 10**9 + 7

def ddprint(x):
  if DBG:
    print(x)

def f(k,p):
  return (c[p] >= k*p)

def ff(k,p):
  acc = n 
  for i in range(len(b)):
    if b[i]>p:
      acc -= b[i]-p 
    else:
      break
  return (acc >= k*p)

n = inn()
a = inl()
h = {}
for x in a:
  if x in h:
    h[x] += 1
  else:
    h[x] = 1
b = []
for x in h:
  b.append(h[x])
b.sort(reverse=True)

#ddprint(b)

c = [0]*(n+1)
for p in range(1,n+1):
  acc = n 
  for i in range(len(b)):
    if b[i]>p:
      acc -= b[i]-p 
    else:
      break
  c[p] = acc


for k in range(1,n+1):
  mn = 0
  mx = n//k + 1
  while mx > mn+1:
    mid = (mn+mx)//2
    if f(k,mid):
      mn = mid 
    else:
      mx = mid 
  print(mn)
