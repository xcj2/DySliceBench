import sys
input = sys.stdin.readline
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

def comb_mod(n,k,p=MOD):
    ans = 1
    k = min(k,n-k)
    for i in range(k):
        ans = ans * (n-i) * inv[i+1] % p
    return ans

N, K = inpl()
inv = [0]*(N+1)
for n in range(1,N+1):
    inv[n] = inv_mod(n)

for i in range(1,min(K+1,N-K+2)):
    print((comb_mod(K-1,i-1)*comb_mod(N-K+1,i)) % MOD)
for i in range(N-K+2,K+1):
    print(0)