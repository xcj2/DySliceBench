MAX_PRIME = 10**3
is_prime = [1] * MAX_PRIME
primes = []
is_prime[0] = 0
is_prime[1] = 0
for i in range(MAX_PRIME):
    if is_prime[i]:
        primes.append(i)
        for j in range(2, ((MAX_PRIME-1)//i) + 1):
            is_prime[i*j] = 0

def factorization(n):
    factor = {}
    for p in primes:
        if p ** 2 > n:
            break
        while n % p == 0:
            n //= p
            if p not in factor:
                factor[p] = 1
            else:
                factor[p] += 1
    if n > 1:
        factor[n] = 1
    return factor
def extGCD(a, b):
    if b == 0:
        return a, 1, 0
    g, y, x = extGCD(b, a%b)
    y -= a//b * x
    return g, x, y
def moddiv(a, b):
    _, inv, _ = extGCD(b, law)
    return a * inv % law

n = int(input())
a = list(map(int, input().split()))

ans = 0
l = {}
lmod = 1
law = 10 ** 9 + 7
for x in a:
    fx = factorization(x)
    for p, c in fx.items():
        if p not in l:
            ans *= p ** c
            lmod *= p ** c
            ans %= law
            lmod %= law
            l[p] = c
        elif c > l[p]:
            ans *= p ** (c - l[p])
            lmod *= p ** (c - l[p])
            ans %= law
            lmod %= law
            l[p] = c
    b = moddiv(lmod, x)
    ans += b
    ans %= law
print(ans)