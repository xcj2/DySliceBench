MOD = int (1e9) + 7
N, K = list (map (int, input().split()))
a = sorted (list (map (int, input().split())))

f = [1 for i in range (N + 1)]

maxSum, minSum = 0, 0

def modPow (base, k) :
    res = 1
    while k : 
        if k & 1 :
            res = res * base % MOD
        base = base * base % MOD
        k >>= 1
    return res

def inv (x) :
    return modPow (x, MOD - 2)

def C (n, m) :
    return (f[n] * inv (f[m]) % MOD) * inv (f[n - m])

if K == 1 :
    print (0)
else :
    for i in range (2, N + 1) :
        f[i] = f[i - 1] * i % MOD
    for i in range (K - 1, N) :
        maxSum = (maxSum + a[i] * C (i, K - 1) % MOD) % MOD
    for i in range (N - K + 1) :
        minSum = (minSum + a[i] * C (N - i - 1, K - 1) % MOD) % MOD
    
    print ((maxSum - minSum + MOD) % MOD)