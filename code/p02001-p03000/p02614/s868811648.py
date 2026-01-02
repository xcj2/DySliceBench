from math import *
from cmath import rect

def dft(f,x):
  if len(f)==1:
    return
  f0,f1=f[0::2],f[1::2]
  dft(f0,x)
  dft(f1,x)
  z=rect(1,x*2*acos(-1)/len(f))
  n=1+0j
  for i in range(len(f)):
    f[i]=f0[i%len(f0)]+n*f1[i%len(f1)]
    n=n*z

def pm(p,q):
  siz=1
  while len(p)+len(q)>siz:
    siz*=2
  np=[]
  nq=[]
  for i in range(len(p)):
    np.append(rect(p[i],0))
  for i in range(len(q)):
    nq.append(rect(q[i],0))
  while len(np)<siz:
    np.append(0+0j)
  while len(nq)<siz:
    nq.append(0+0j)
  dft(np,1)
  dft(nq,1)
  for i in range(siz):
    np[i]=np[i]*nq[i]
  dft(np,-1)
  EPS=0.1
  for i in range(siz):
    np[i]=int(np[i].real/siz+EPS)
  return np

H,W,K=map(int,input().split())
C=[input() for i in range(H)]
DP=0
X=[]
P=0

def poly(x):
  r=[0]*x
  r.append(1)
  r[0]+=1
  return r

def knapsack(L):
  if len(L)==1:
    return poly(L[0])
  a=knapsack(L[:len(L)//2])
  b=knapsack(L[len(L)//2:])
  return pm(a,b)[:K+1]

for i in range(1,1<<H):
  X=[0]*W
  for j in range(H):
    if i&(1<<j):
      for k in range(W):
        if C[j][k]=='#':
          X[k]+=1
  DP=knapsack(X)
  if len(DP)>K:
    P+=DP[K]
print(P)