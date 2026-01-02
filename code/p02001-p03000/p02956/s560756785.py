import sys
input=lambda: sys.stdin.readline().rstrip()
n=int(input())
mod=998244353
from collections import defaultdict
DX=defaultdict(int)
DY=defaultdict(int)
XY,X,Y=[],[],[]
for _ in range(n):
  x,y=map(int,input().split())
  X.append(x)
  Y.append(y)
  XY.append((x,y))
X.sort()
Y.sort()
XY.sort(key=lambda x:x[0])
for i,x in enumerate(X):
  DX[x]=i+1
for i,y in enumerate(Y):
  DY[y]=i+1
XY2=[]
for x,y in XY:
  XY2.append((DX[x],DY[y]))
A=[[0]*4 for _ in range(n)]

n_max=2*10**5
nn=n_max.bit_length()+1
BIT=[0]*(2**nn)
BIT.insert(0,0)
def bitsum(BIT,i):
  s=0
  while i>0:
    s+=BIT[i]
    i-=i&(-i)
  return s
def bitadd(BIT,i,x):
  while i<=2**nn:
    BIT[i]+=x
    i+=i&(-i)
  return BIT

for i in range(n):
  x,y=XY2[i]
  ct=bitsum(BIT,y)
  A[i][2]+=ct
  A[i][1]+=i-ct
  bitadd(BIT,y,1)

BIT=[0]*(2**nn)
BIT.insert(0,0)
for i in range(n)[::-1]:
  x,y=XY2[i]
  ct=bitsum(BIT,y)
  A[i][3]+=ct
  A[i][0]+=(n-1-i)-ct
  bitadd(BIT,y,1)

P=[0]*n
P[0]=1
for i in range(1,n):
  P[i]=(P[i-1]*2)%mod
def f(x):
  return P[x]

ans=0
for a,b,c,d in A:
  ans+=2*f(a+b+c+d)-f(a+b)-f(b+c)-f(c+d)-f(d+a)+f(a)+f(b)+f(c)+f(d)-1
  ans%=mod
print(ans)
