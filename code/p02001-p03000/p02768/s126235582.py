MOD = 10**9+7
def inv_mod(a,p=MOD):
    def inv_mod_sub(a,p):
        if a == 1:
            return 1,0
        else:
            d,r = p//a,p%a
            x,y = inv_mod_sub(r,a)
            return y-d*x,x
    if p < 0: p = -p
    a %= p
    return inv_mod_sub(a,p)[0] % p

def comb_mod(n,k):
    if k < 0 or k > n:
        return 0
    else:
        c = 1
        for i in range(k):
            c *= n-i
            c %= MOD
        return c*f_mod_inverse[k] % MOD
f_mod=[1]*(10**6)
f_mod_inverse=[1]*(10**6)
for i in range(1,10**6):
  f_mod[i]=f_mod[i-1]*i%MOD
  f_mod_inverse[i]=f_mod_inverse[i-1]*inv_mod(i)%MOD
n,a,b = map(int,input().split())
print((pow(2,n,MOD)-comb_mod(n,a)-comb_mod(n,b)-1)%MOD)