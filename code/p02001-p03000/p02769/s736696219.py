import sys
sys.setrecursionlimit(10**9)

MOD=10**9+7
n,k=map(int,input().split())

def pow_mod(x,n):
  if n==0:
    return 1
  elif n==1:
    return x
  else:
    xn2=pow_mod(x,n//2)
    if n%2==0:
      return (xn2*xn2)%MOD
    else:
      return (xn2*xn2*x)%MOD

def fact_mod(a):
  if a<=1:
    return 1
  else:
    return a*fact_mod(a-1)%MOD
  
def perm_mod(n,a):
  if a==1:
    return n
  else:
    return (n*perm_mod(n-1,a-1))%MOD

def inv_mod(a):
  return pow_mod(a,MOD-2)%MOD
  
def comb_mod(na,fa):
  ainv=inv_mod(fa)
  return (na*ainv)%MOD
  
if k>=n-1:  
  #nHn=(2n-1)Cn
  perm=perm_mod(2*n-1,n)
  fact=fact_mod(n)
  comb=comb_mod(perm,fact)
  #print(perm,fact,comb)
  print(comb)
else:
  inv_table = [0]+[1]
  for i in range(2,k+1):
    inv_table+=[inv_table[MOD%i]*(MOD-int(MOD/i))%MOD]
  
  comb_sum=1
  fact=1
  comb1=1
  comb2=1
  for i in range(1,k+1):
    #comb1=comb1*(n-i+1)//i
    comb1=(comb1*(n-i+1)*inv_table[i])%MOD
    #comb2=comb2*(n-i)//i
    comb2=(comb2*(n-i)*inv_table[i])%MOD
    comb=(comb1*comb2)%MOD
    comb_sum+=comb
  
  print(comb_sum%MOD)
