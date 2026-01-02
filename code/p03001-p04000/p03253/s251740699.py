import sys
n,m=map(int,input().split())
MOD = 10**9+7
ans=1
if m==1:
  print(1)
  sys.exit()
def inv_mod(a, p=MOD):
    def inv_mod_sub(a, p):
        if a == 1:
            return 1, 0
        else:
            d, r = p//a, p%a
            x, y = inv_mod_sub(r, a)
            return y-d*x, x
    if p < 0: p = -p
    a %= p
    return inv_mod_sub(a,p)[0] % p

def comb_mod(n, k):
    if k < 0 or k > n:
        return 0
    else:
        return f_mod[n]*f_mod_inverse[k]*f_mod_inverse[n-k] % MOD
pf={}
for i in range(2,int(m**0.5)+1):
    while m%i==0:
        pf[i]=pf.get(i,0)+1
        m//=i
if m>1:pf[m]=1
Max=max(list(pf.values()))
f_mod=[1]*(Max+n+1)
f_mod_inverse=[1]*(Max+n+1)
for i in range(1,Max+n+1):
  f_mod[i]=(f_mod[i-1]*i)%MOD
  f_mod_inverse[i]=(f_mod_inverse[i-1]*inv_mod(i)) % MOD  
for i in pf.values():
  ans*=comb_mod(i+n-1,n-1)
print(ans%MOD)
