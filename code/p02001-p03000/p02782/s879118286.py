import sys
readline = sys.stdin.buffer.readline
r1,c1,r2,c2 = map(int,readline().split())
mod = 10**9+7
def pow(n,p,mod=10**9+7): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2 % mod
            p //= 2
        else:
            res = res * n % mod
            p -= 1
    return res % mod
def factrial_memo(n=3*10**6+1,mod=10**9+7):
    fact = [1, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % mod)
    return fact
def fermat_cmb(n, r, mod=10**9+7): #needs pow,factrial_memo(only fact). return nCk
    return fact[n] * pow(fact[r],mod-2) * pow(fact[n-r],mod-2) %mod
fact = factrial_memo()
r1,c1,r2,c2 = r1+1,c1+1,r2+1,c2+1
al = fermat_cmb(r2+c2,r2)
sub_r = fermat_cmb(r1-1+c2,r1-1)
sub_c = fermat_cmb(r2+c1-1,c1-1)
add_rc = fermat_cmb(r1-1+c1-1,r1-1)

al -= sub_r+sub_c
al += add_rc

print(al%mod)