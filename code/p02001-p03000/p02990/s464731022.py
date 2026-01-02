inpl = lambda: list(map(int,input().split()))
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
        return factorial_mod[n]*factorial_inv_mod[k]*factorial_inv_mod[n-k] % MOD

N, K = inpl()
factorial_mod = [1]*(N+1)
factorial_inv_mod = [1]*(N+1)
for n in range(1,N+1):
    factorial_mod[n] = factorial_mod[n-1]*n % MOD
    factorial_inv_mod[n] = factorial_inv_mod[n-1]*inv_mod(n) % MOD

for i in range(1,K+1):
    print((comb_mod(K-1,i-1)*comb_mod(N-K+1,i)) % MOD)