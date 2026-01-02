def gcd(a, b):
    while b: a, b = b, a % b
    return a
def isPrimeMR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1<<32 else [2, 3, 5, 7, 11, 13, 17] if n < 1<<48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1: continue
        while y != n - 1:
            y = y * y % n
            if y == 1 or t == n - 1: return 0
            t <<= 1
    return 1
def findFactorRho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):
        f = lambda x: (x * x + c) % n
        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if isPrimeMR(g): return g
            elif isPrimeMR(n // g): return n // g
            return findFactorRho(g)
def primeFactor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k: ret[i] = k
        i += i % 2 + (3 if i % 3 == 1 else 1)
        if i == 101 and n >= 2 ** 20:
            while n > 1:
                if isPrimeMR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = findFactorRho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k

    if n > 1: ret[n] = 1
    if rhoFlg: ret = {x: ret[x] for x in sorted(ret)}
    return ret

def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p]+1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)

def exEuclid(a, mod):
    b = mod
    s, u = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        s, u = u, s - q * u
    return a, s % mod

def crt(R, M):
    assert len(R) == len(M)
    N = len(R)
    r0, m0 = 0, 1
    for r, m in zip(R, M):
        assert m >= 1
        r %= m
        if m0 < m:
            r0, r = r, r0
            m0, m = m, m0
        if m0 % m == 0:
            if r0 % m != r: return (0, 0)
            continue
        g, im = exEuclid(m0, m)
        u = m // g
        if (r - r0) % g: return (0, 0)
        x = (r - r0) // g % u * im % u
        r0 += x * m0
        m0 *= u
        if r0 < 0: r0 += m0
    return (r0, m0)


N = int(input())
if N <= 10:
    for i in range(1, 100):
        if i * (i + 1) // 2 % N == 0:
            print(i)
            exit()
pf = primeFactor(N)
# print("pf =", pf)
L = []
for p in pf:
    L.append(p ** pf[p])
# print("L =", L)
k = len(L)
mi = 10 ** 100
for i in range(1 << k):
    R, M = [], []
    for j, m in enumerate(L):
        if i >> j & 1:
            R.append(0)
        else:
            R.append(m - 1)
        M.append(m)
    c = crt(R, M)[0]
    if c and c * (c + 1) // 2 % N == 0:
        mi = min(mi, c)
print(mi)