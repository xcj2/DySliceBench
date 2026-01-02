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

# nがある程度小さい時(10^7程度)
def modcombination(n, k, mod):
    fact = [1 for _ in range(n+1)]
    inv = [1 for _ in range(n+1)]
    finv = [1 for _ in range(n+1)]

    for i in range(2, n+1):
        fact[i] = (fact[i-1] * i) % mod
        inv[i] = (-inv[mod % i] * (mod // i)) % mod
        finv[i] = (finv[i-1] * inv[i]) % mod
    return fact[n] * (finv[k] * finv[n-k] % mod) % mod

# kが小さい時
def modcombination_smallk(n, k, mod):
    result = 1
    for i in range(k):
        result = (((result * (n-i))%mod) * modinv(i+1, mod))%mod
    return result

n, a, b = [int(i) for i in input().split()]
mod = (10**9)+7
# 全部でn**2(0本は除くかも)
# a本を選ぶ場合の数はnCa
total = modpow(2, n, mod)
tota = modcombination_smallk(n, a, mod)
totb = modcombination_smallk(n, b, mod) 
print((total-tota-totb-1)%mod)