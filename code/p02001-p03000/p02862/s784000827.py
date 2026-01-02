MOD=10**9+7
X,Y=map(int,input().split())

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

if (X+Y)%3!=0:
  print(0)
else:
  u=(2*X-Y)//3
  v=(-X+2*Y)//3
  if u>=0 and v>=0:    
    #print(u,v)
    print(comb_mod(u+v,v))
  else:
    print(0)