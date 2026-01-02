from collections import Counter, defaultdict
# 拡張ユークリッド互除法
# ax + by = gcd(a,b)の最小整数解を返す
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# mを法とするaの乗法的逆元
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# 素因数分解
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            yield i
    if n > 1:
        yield n

# mを法とするときのa^n
def modpow(a,n,m):
    res = 1
    t = a
    while n:
        if n%2:
            res = (res*t)%m
        t = (t*t)%m
        n //= 2
    return res

def lcm_mod(nums, mod):
    p = defaultdict(int)
    for n in nums:
        c = Counter(prime_factors(n))
        for v,cnt in c.items():
            p[v] = max(p[v],cnt)

    res = 1
    for v,cnt in p.items():
        res *= modpow(v,cnt,mod)
        res %= mod
    return res


MOD = 10**9+7

N = int(input())
A = list(map(int,input().split()))

s = sum(modinv(a,MOD) for a in A)%MOD

s *= lcm_mod(A, MOD)
print(s%MOD)
