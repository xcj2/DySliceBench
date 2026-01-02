#Convolution_998244353

MOD = 998244353
ROOT = 3

sum_e = (911660635, 509520358, 369330050, 332049552, 983190778, 123842337, 238493703, 975955924, 603855026, 856644456, 131300601, 842657263, 730768835, 942482514, 806263778, 151565301, 510815449, 503497456, 743006876, 741047443, 56250497, 0, 0, 0, 0, 0, 0, 0, 0, 0)
sum_ie = (86583718, 372528824, 373294451, 645684063, 112220581, 692852209, 155456985, 797128860, 90816748, 860285882, 927414960, 354738543, 109331171, 293255632, 535113200, 308540755, 121186627, 608385704, 438932459, 359477183, 824071951, 0, 0, 0, 0, 0, 0, 0, 0, 0)

def butterfly(arr):
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p] * now
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (l - r) % MOD
            now *= sum_e[(~s & -~s).bit_length() - 1]
            now %= MOD

def butterfly_inv(arr):
    n = len(arr)
    h = (n - 1).bit_length()
    for ph in range(1, h + 1)[::-1]:
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p]
                arr[i + offset] = (l + r) % MOD
                arr[i + offset + p] = (MOD + l - r) * inow % MOD
            inow *= sum_ie[(~s & -~s).bit_length() - 1]
            inow %= MOD

def convolution(a, b):
    n = len(a)
    m = len(b)
    if not n or not m: return []
    if min(n, m) <= 100:
        if n < m:
            n, m = m, n
            a, b = b, a
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i + j] += a[i] * b[j]
                res[i + j] %= MOD
        return res
    z = 1 << (n + m - 2).bit_length()
    a += [0] * (z - n)
    b += [0] * (z - m)
    butterfly(a)
    butterfly(b)
    for i in range(z):
        a[i] *= b[i]
        a[i] %= MOD
    butterfly_inv(a)
    a = a[:n + m - 1]
    iz = pow(z, MOD - 2, MOD)
    for i in range(n + m - 1):
        a[i] *= iz
        a[i] %= MOD
    return a

def autocorrelation(a):
    n = len(a)
    if not n: return []
    if n <= 100:
        res = [0] * (2 * n - 1)
        for i in range(n):
            for j in range(n):
                res[i + j] += a[i] * a[j]
                res[i + j] %= MOD
        return res
    z = 1 << (2 * n - 2).bit_length()
    a += [0] * (z - n)
    butterfly(a)
    for i in range(z):
        a[i] *= a[i]
        a[i] %= MOD
    butterfly_inv(a)
    a = a[:2 * n - 1]
    iz = pow(z, MOD - 2, MOD)
    for i in range(2 * n - 1):
        a[i] *= iz
        a[i] %= MOD
    return a

def resize(a, m):
    n = len(a)
    if n == m: return a
    if n > m: return a[:m]
    else: return a + [0] * (m - n)

def add(a, b):
    return [(va + vb) % MOD for va, vb in zip(a, b)]

def sub(a, b):
    return [(va - vb) % MOD for va, vb in zip(a, b)]

def times(a, k):
    return [v * k % MOD for v in a]

def multiply(a, b):
    return convolution(a.copy(), b.copy())

def square(a):
    return autocorrelation(a.copy())

def inverse(a):
    n = len(a)
    r = pow(a[0], MOD - 2, MOD)
    m = 1
    tmp = [r]
    while m < n:
        tmp += [0] * m
        m *= 2
        tmp = sub(times(tmp, 2), multiply(a[:m], square(tmp.copy())[:m]))
    res = tmp[:n]
    return res

def divide(a, b):
    return multiply(a, inverse(b))

def differentiate(a):
    n = len(a)
    res = [0] * n
    for i in range(1, n):
        res[i - 1] = a[i] * i % MOD
    return res

def integrate(a):
    n = len(a)
    res = [0] * n
    for i in range(n - 1):
        res[i + 1] = a[i] * pow(i + 1, MOD - 2, MOD) % MOD
    return res

def log(a):
    assert a[0] == 1
    n = len(a)
    return integrate(divide(differentiate(a), a)[:n])

def exp(a):
    assert a[0] == 0
    n = len(a)
    res = [1]
    g = [1]
    q = differentiate(a)
    m = 1
    while m < n:
        g = sub(times(g, 2), multiply(res, square(g)[:m]))
        g += [0] * m
        res += [0] * m
        m *= 2
        w = add(q[:m], multiply(g, sub(differentiate(res), multiply(res, q[:m])[:m]))[:m])
        res = add(res, multiply(res, sub(a[:m], integrate(w)))[:m])
    return res[:n]

def power(a, k):
    n = len(a)
    for d, p in enumerate(a):
        if p != 0: break
    else: return [0] * n
    res = [0] * n
    g = a[d:] + [0] * d
    g = exp(times(log(times(g, pow(p, MOD - 2, MOD))), k))
    for i in range(max(n - d * k, 0)):
        res[d * k + i] = g[i]
    res = times(res, pow(p, k, MOD))
    return res

def tonelli_shanks(n, p): #n < p
    if n == 0: return 0
    if n == 1: return 1
    if pow(n, (p - 1) // 2, p) != 1: return -1
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 1
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(n, q, p), pow(n, (q + 1) // 2, p)
    while t != 1:
        k = 1
        while pow(t, 2**k, p) != 1:
            k += 1
        x = pow(c, pow(2, m - k - 1, p - 1), p)
        m = k
        c = (x * x) % p
        t = (t * c) % p
        r = (r * x) % p
    if r * r % p != n: return -1
    return r

def sqrt_(a):
    assert a[0] != 0
    n = len(a)
    s = tonelli_shanks(a[0], MOD)
    if s == -1: return
    m = 1
    res = [s]
    minv2 = pow(2, MOD - 2, MOD)
    while m < n:
        res += [0] * m
        m *= 2
        res = times(add(res, divide(a[:m], res)), minv2)
    return res[:n]

def sqrt(a):
    n = len(a)
    for d, p in enumerate(a):
        if p != 0: break
    else: return [0] * n
    if d % 2 == 1: return
    s = tonelli_shanks(p, MOD)
    if s == -1: return
    res = [0] * n
    g = a[d:] + [0] * d
    g = sqrt_(times(g, pow(p, MOD - 2, MOD)))
    if g is None: return
    g = times(g, s)
    for i in range(n - d + 1):
        if d // 2 + i >= n: break
        res[d // 2 + i] = g[i]
    return res

def build_exp(n, b):
    res = [0] * (n + 1)
    res[0] = 1
    for i in range(n):
        res[i + 1] = res[i] * b % MOD
    return res

def build_factorial(n):
    fct = [0] * (n + 1)
    inv = [0] * (n + 1)
    fct[0] = inv[0] = 1
    for i in range(n):
        fct[i + 1] = fct[i] * (i + 1) % MOD
    inv[n] = pow(fct[n], MOD - 2, MOD)
    for i in range(n)[::-1]:
        inv[i] = inv[i + 1] * (i + 1) % MOD
    return fct, inv

def taylor_shift(a, c):
    n = len(a)
    fct, inv = build_factorial(n)
    d = build_exp(n, c)
    p = [0] * (2 * n - 1)
    for i in range(n):
        p[i + n - 1] = a[i] * fct[i] % MOD
    q = [0] * (2 * n - 1)
    for i in range(n):
        q[n - 1 - i] = d[i] * inv[i] % MOD
    r = multiply(p, q)
    res = [0] * n
    for i in range(n):
        res[i] = r[2 * n - 2 + i] * inv[i] % MOD
    return res

def bernoulli(n):
    fct, inv = build_factorial(n + 1)
    e = [0] * n
    e[0] = 1
    expx = [inv[i + 1] for i in range(n)]
    res = [v * fct[i] % MOD for i, v in enumerate(divide(e, expx)[:n])]
    return res

def partition(n):
    res = [0] * n
    for i in range(-n, n + 1):
        k = i * (3 * i - 1) // 2
        if k >= n: continue
        if i % 2 == 0: res[k] = 1
        else: res[k] = MOD - 1
    return inverse(res)

def stirling_first(n):
    res = [1]
    t = 0
    for i in range((n).bit_length())[::-1]:
        a = n >> i
        res = multiply(res, taylor_shift(res, -t))
        t *= 2
        if a & 1:
            res = multiply(res, [-t, 1])
            t += 1
    return res

def stirling_second(n):
    fct, inv = build_factorial(n + 1)
    a = [0] * (n + 1)
    b = [0] * (n + 1)
    for i in range(n + 1):
        a[i] = pow(i, N, MOD) * inv[i] % MOD
        b[i] = inv[i] * (1 - (i & 1) * 2)
    res = multiply(a, b)[:n + 1]
    return res

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
F = [0] * (N + 1)

for _ in range(K):
    l, r = map(int, input().split())
    for i in range(l, r + 1):
        F[i] = 1

I = [1] + [0] * N

print(inverse(sub(I, F))[N - 1])