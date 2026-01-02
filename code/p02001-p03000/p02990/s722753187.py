N_MAX = 200000
MOD = 10**9 + 7
fac, finv, inv = [0]*N_MAX, [0]*N_MAX, [0]*N_MAX
def com_init():
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, N_MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

def com(n, k):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD



def main():
    n, k = map(int, input().split()) 
    if n == k:
        for i in range(1,k+1):
            if i==1:print(1)
            else:print(0)
        return
    com_init()
    for i in range(1,k+1):
        b = k
        r = n-k
        ans = com(b-1,i-1) * com(r-1, i-1) * 2 + com(b-1,i-1) * com(r-1, i-1-1) + com(b-1,i-1) * com(r-1, i+1-1)
        print(ans%MOD)
    
if __name__ == "__main__":
    main()