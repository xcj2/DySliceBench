h,w,a,b=map(int,input().split())
n=h+w
MOD = 10**9+7

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
f_mod=[1]*(n+1)
f_mod_inverse=[1]*(n+1)
for i in range(1,n+1):
  f_mod[i]=f_mod[i-1]*i%MOD
  f_mod_inverse[i]=f_mod_inverse[i-1]*inv_mod(i)%MOD

ans=0
for i in range(h-a):
    ans+=(comb_mod(i+b-1,i)*comb_mod(w-b-1+h-i-1,h-i-1))%MOD
print(ans%MOD)
