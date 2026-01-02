import math
MOD=10**9+7

def powmod(a,p):
  if p==0:
    return 1
  elif p==1:
    return a
  else:
    pow2=powmod(a,p//2)
    if p%2==0:
      return (pow2**2)%MOD
    else:
      return (a*pow2**2)%MOD

def invmod(a):
  return powmod(a,MOD-2)

def comb_mod(n,r):
  nPr=1
  fact_r=1
  for i in range(r):
    nPr*=n-i
    nPr%=MOD
    fact_r*=r-i
    fact_r%=MOD  
  return (nPr*invmod(fact_r))%MOD

N,M=map(int,input().split())
fact={}
for i in range(2,int(math.sqrt(M))+1):
  if M==1:
    break
  while(M%i==0):
    M//=i
    if not i in fact:
      fact[i]=1
    else:
      fact[i]+=1  
if M!=1:
  fact[M]=1
  
#print(fact)
answer=1
for r in fact.values():
  answer*=comb_mod(N+r-1,r)
  answer%=MOD
  
print(answer)