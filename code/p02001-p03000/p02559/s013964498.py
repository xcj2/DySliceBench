def Binit(B,siz):
  while len(B)<siz+1:
    B.append(0)
  while len(B)>siz+1:
    del B[-1]
  for i in range(siz+1):
    B[i]=0
  B.append(siz)

def Badd(B,a,x):
  z=a
  while z<=B[-1]:
    B[z]+=x
    z+=(z&(-z))

def Bsum(B,a):
  r=0
  z=a
  while z>0:
    r+=B[z]
    z-=(z&(-z))
  return r

def Bssum(B,a,b):
  return Bsum(B,max(a,b))-Bsum(B,min(a,b)-1)

BIT=[]
N,Q=map(int,input().split())
Binit(BIT,N+1)
A=list(map(int,input().split()))
for i in range(N):
  Badd(BIT,i+1,A[i])
a,b,c=0,0,0
for i in range(Q):
  a,b,c=map(int,input().split())
  if a:
    print(Bssum(BIT,b+1,c))
  else:
    Badd(BIT,b+1,c)