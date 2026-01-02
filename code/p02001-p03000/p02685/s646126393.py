def modpow(a, n, mod):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return (modpow((a * a)%mod, n//2, mod)) % mod
        else:
            return ((a%mod) * modpow(a, n-1, mod)) % mod

# modが素であるとする
def modinv(a, mod):
    return modpow(a, mod-2, mod) % mod

def moddiv(a, b, mod):
    return ((a%mod) * modinv(b, mod)) % mod

def modbase(n, k, mod):
    fact = [1 for _ in range(n+1)]
    inv = [1 for _ in range(n+1)]
    finv = [1 for _ in range(n+1)]

    for i in range(2, n+1):
        fact[i] = (fact[i-1] * i) % mod
        inv[i] = (-inv[mod % i] * (mod // i)) % mod
        finv[i] = (finv[i-1] * inv[i]) % mod
    return fact, inv,finv


N, M, K = [int(i) for i in input().split()]
mod = 998244353
# N-1 V K
fact, inv, finv = modbase(N-1, K, mod)
dic = {}
dic[0] = 1
for k in range(1, K+1):
    dic[k] = fact[N-1] * (finv[k] * finv[N-k-1] % mod) % mod

sum = 0
for k in range(K+1):
    sum += M * (modpow(M-1 , N-1-k, mod) * dic[k] % mod) % mod
    sum %= mod
print(sum)
