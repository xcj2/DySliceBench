
# sum(nCm) 
# 1:1 1 = 2     2
# 2:1 2 1 = 4
# 3:1 3 3 1 = 8  (1+x)**3
# 4:1 4 6 4 1 = 16
# 5:1 5 10 10 5 1 = 32 (1+x)^5

MOD = 1000000007

def modpow(a, n):
    res = 1
    while n > 0:
        if n & 1:
            res = (res * a) % MOD
        a = (a * a) % MOD
        n = n >> 1
    return res

def modinv(a):
    return modpow(a, MOD-2)

def fact(k):
    d = 1
    for i in range(1, k+1):
        d = (d * i) % MOD
    return d

def C(n, k):
    p = 1
    for i in range(n-k+1, n+1):
        p = (p * i) % MOD
    d = 1
    for i in range(1, k+1):
        d = (d * i) % MOD
    return (p * modinv(d)) % MOD
#for i in range(1, 13): print(modinv(i))
n, a, b = map(int, input().split())
base = modpow(2, n)
base = (base - C(n,a)) % MOD
base = (base - C(n, b)) % MOD
print(base-1)
