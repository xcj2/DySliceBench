import sys
sys.setrecursionlimit(10**9)

MOD=10**9+7
n,a,b=map(int,input().split())

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
  
num_all=pow_mod(2,n)-1
perm_na=perm_mod(n,a)
fact_a=fact_mod(a)
comb_na=comb_mod(perm_na,fact_a)
#print(perm_na,fact_a,comb_na)
perm_nb=perm_mod(n,b)
fact_b=fact_mod(b)
comb_nb=comb_mod(perm_nb,fact_b)
#print(perm_nb,fact_b,comb_nb)
#print(num_all,comb_na,comb_nb)
print((num_all-comb_na-comb_nb+MOD)%MOD)