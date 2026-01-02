#import numpy as np

n,a,b=map(int,input().split())
#M=10**8
M=2*10**5+1
Mod=10**9+7
fac=[0]*M
finv=[0]*M
inv=[0]*M
ans=pow(2,n,Mod)-1

#finvに逆元、facに階乗のmod
"""
def COMinit():
  fac[0]=fac[1]=1
  finv[0]=finv[1]=1
  inv[1]=1
  for i in range(2,M):
    fac[i]=(fac[i-1]*i%Mod)%Mod
    inv[i]=Mod-inv[Mod%i]*(Mod//i) %Mod
    finv[i]=(finv[i-1]*inv[i]%Mod)%Mod
"""

def COMinit():
  fac[0]=n%Mod
  fac[1]=(fac[0]*(n-1))%Mod
  finv[0]=finv[1]=1
  inv[1]=1
  for i in range(2,M):
    fac[i]=(fac[i-1]%Mod*(n-i))%Mod
    inv[i]=Mod-inv[Mod%i]*(Mod//i) %Mod
    finv[i]=(finv[i-1]*inv[i]%Mod)%Mod
def COM(n,k):
  if n<k:
    return 0
  if n<0 or k<0:
    return 0
  return (fac[k-1]*(finv[k]%Mod))%Mod

COMinit()
ans-=(COM(n,a)+COM(n,b))
print(ans%Mod)
