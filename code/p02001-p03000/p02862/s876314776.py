x,y=map(int,input().split())
MOD = 10**9+7
if (x+y)%3!=0:print(0);exit()
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
f_mod=[1]*(10**6)
f_mod_inverse=[1]*(10**6)
for i in range(1,10**6):
  f_mod[i]=f_mod[i-1]*i%MOD
  f_mod_inverse[i]=f_mod_inverse[i-1]*inv_mod(i)%MOD
cnt=(x+y)//3
dif=abs(x-y)
ele=(cnt-dif)//2
print(comb_mod(cnt,ele))