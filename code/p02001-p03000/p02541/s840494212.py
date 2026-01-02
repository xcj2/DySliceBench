def prime_factor(n):
    factors = {}
    if n % 2 == 0:
        cnt = 0
        while n % 2 == 0:
            cnt += 1
            n //= 2
        factors[2] = cnt
    i = 3
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            factors[i] = cnt
        i += 2
    if n != 1:
        factors[n] = 1
    return factors

def extgcd(a, b):
    s, sx, sy, t, tx, ty = a, 1, 0, b, 0, 1
    while t:
        q = s // t
        s -= t * q
        s, t = t, s
        sx -= tx * q
        sx, tx = tx, sx
        sy -= ty * q
        sy, ty = ty, sy
    return sx, sy

def calc(a, b):
    x, y = extgcd(-a, b)
    if x < 0:
        k = (-x + b - 1) // b
        x += b * k
        y += a * k
    if x == 0:
        x += b
        y += a
    if y < 0:
        k = (-y + a - 1) // a
        x += b * k
        y += a * k
    if y == 0:
        x += b
        y += a
    return x, y

N = int(input())
primes = prime_factor(2 * N)
ans = float('inf')
for S in range(1 << len(primes)):
    a = b = 1
    for i, (p, c) in enumerate(primes.items()):
        if S >> i & 1:
            a *= pow(p, c)
        else:
            b *= pow(p, c)
    x, y = calc(a, b)
    ans = min(ans, a * x)
    x, y = calc(b, a)
    ans = min(ans, b * x)
print(ans)

