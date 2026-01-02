def COMinit(N, mod):
    fac = [0] * N
    finv = [0] * N
    inv = [0] * N

    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1

    for i in range(2, N):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod
    
    return fac, finv, inv

def COM(n, r, mod, fac, finv, inv):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n-r] % mod) % mod

def solve():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    MOD = 10**9 + 7
    A.sort()

    fac, finv, inv = COMinit(N+1,MOD)
    max_sm = 0
    min_sm = 0
    for i in range(N):
        smallerNums = i
        largerNums = N - i - 1
        max_sm += A[i] * COM(smallerNums, K-1, MOD, fac, finv, inv) % MOD
        min_sm += A[i] * COM(largerNums, K-1, MOD, fac, finv, inv) % MOD
    
    print((max_sm % MOD - min_sm % MOD) % MOD)

if __name__ == '__main__':
    solve()