def primitive_root(m):
    if m == 2: return 1
    if m == 167772161: return 3
    if m == 469762049: return 3
    if m == 754974721: return 11
    if m == 998244353: return 3
    divs = [0] * 20
    cnt = 1
    x = (m - 1) // 2
    while x % 2 == 0:
        x //= 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            divs[cnt] = i
            cnt += 1
            while x % i == 0:
                x //= i
        i += 2
    if x > 1:
        divs[cnt] = x
        cnt += 1
        g = 2
    while True:
        ok = True
        for i in range(cnt):
            if pow(g, (m - 1) // divs[i], m) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1

def inv_gcd(a, b):
    a %= b
    if a == 0: return b, 0
    s = b
    t = a
    m0 = 0
    m1 = 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0: m0 += b // s
    return s, m0

def butterfly(arr, mod):
    g = primitive_root(mod)
    n = len(arr)
    h = (n - 1).bit_length()
    first = True
    sum_e = [0] * 30
    if first:
        first = False
        es = [0] * 30
        ies = [0] * 30
        m = mod - 1
        cnt2 = (m & -m).bit_length() - 1
        e = pow(g, m >> cnt2, mod)
        ie = pow(e, mod - 2, mod)
        for i in range(cnt2 - 1)[::-1]:
            es[i] = e
            ies[i] = ie
            e *= e
            e %= mod
            ie *= ie
            ie %= mod
        now = 1
        for i in range(cnt2 - 2):
            sum_e[i] = es[i] * now % mod
            now *= ies[i]
            now %= mod
    for ph in range(1, h + 1):
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        now = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p] * now
                arr[i + offset] = (l + r) % mod
                arr[i + offset + p] = (l - r) % mod
            now *= sum_e[(~s & -~s).bit_length() - 1]
            now %= mod

def butterfly_inv(arr, mod):
    g = primitive_root(mod)
    n = len(arr)
    h = (n - 1).bit_length()
    first = True
    sum_ie = [0] * 30
    if first:
        first = False
        es = [0] * 30
        ies = [0] * 30
        m = mod - 1
        cnt2 = (m & -m).bit_length() - 1
        e = pow(g, m >> cnt2, mod)
        ie = pow(e, mod - 2, mod)
        for i in range(cnt2 - 1)[::-1]:
            es[i] = e
            ies[i] = ie
            e *= e
            e %= mod
            ie *= ie
            ie %= mod
        now = 1
        for i in range(cnt2 - 2):
            sum_ie[i] = ies[i] * now % mod
            now *= es[i]
            now %= mod
    for ph in range(1, h + 1)[::-1]:
        w = 1 << (ph - 1)
        p = 1 << (h - ph)
        inow = 1
        for s in range(w):
            offset = s << (h - ph + 1)
            for i in range(p):
                l = arr[i + offset]
                r = arr[i + offset + p]
                arr[i + offset] = (l + r) % mod
                arr[i + offset + p] = (mod + l - r) * inow % mod
            inow *= sum_ie[(~s & -~s).bit_length() - 1]
            inow %= mod

def convolution(a, b, mod=998244353):
    n = len(a)
    m = len(b)
    if not n or not m: return []
    if min(n, m) <= 60:
        if n < m:
            n, m = m, n
            a, b = b, a
        res = [0] * (n + m - 1)
        for i in range(n):
            for j in range(m):
                res[i + j] += a[i] * b[j]
                res[i + j] %= mod
        return res
    z = 1 << (n + m - 2).bit_length()
    a += [0] * (z - n)
    b += [0] * (z - m)
    butterfly(a, mod)
    butterfly(b, mod)
    for i in range(z):
        a[i] *= b[i]
        a[i] %= mod
    butterfly_inv(a, mod)
    a = a[:n + m - 1]
    iz = pow(z, mod - 2, mod)
    for i in range(n + m - 1):
        a[i] *= iz
        a[i] %= mod
    return a

def convolution_ll(a, b):
    n = len(a)
    m = len(b)
    if not n or not m: return []
    mod1 = 754974721
    mod2 = 167772161
    mod3 = 469762049
    m2m3 = mod2 * mod3
    m1m3 = mod1 * mod3
    m1m2 = mod1 * mod2
    m1m2m3 = mod1 * mod2 * mod3
    i1 = inv_gcd(m2m3, mod1)[1]
    i2 = inv_gcd(m1m3, mod2)[1]
    i3 = inv_gcd(m1m2, mod3)[1]
    c1 = convolution(a.copy(), b.copy(), mod1)
    c2 = convolution(a.copy(), b.copy(), mod2)
    c3 = convolution(a.copy(), b.copy(), mod3)
    c = [0] * (n + m - 1)
    for i in range(n + m - 1):
        x = 0
        x += (c1[i] * i1) % mod1 * m2m3
        x += (c2[i] * i2) % mod2 * m1m3
        x += (c3[i] * i3) % mod3 * m1m2
        x %= m1m2m3
        c[i] = x
    return c

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*convolution(A, B))