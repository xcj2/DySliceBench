def modinv(x, mod):
    a, b = x, mod
    u, v = 1, 0
    while b:
        t = a // b
        a -= t * b; a, b = b, a
        u -= t * v; u, v = v, u
    return u % mod


def _garner(xs, mods):
    M = len(xs)
    coeffs = [1] * M
    constants = [0] * M
    for i in range(M - 1):
        mod_i = mods[i]
        v = (xs[i] - constants[i]) * modinv(coeffs[i], mod_i) % mod_i
        for j in range(i + 1, M):
            mod_j = mods[j]
            constants[j] = (constants[j] + coeffs[j] * v) % mod_j
            coeffs[j] = (coeffs[j] * mod_i) % mod_j

    return constants[-1]


def bit_reverse(d):
    n = len(d)
    ns = n >> 1
    nss = ns >> 1
    ns1 = ns + 1
    i = 0
    for j in range(0, ns, 2):
        if j < i:
            d[i], d[j] = d[j], d[i]
            d[i + ns1], d[j + ns1] = d[j + ns1], d[i + ns1]
        d[i + 1], d[j + ns] = d[j + ns], d[i + 1]
        k = nss
        i ^= k
        while k > i:
            k >>= 1
            i ^= k
    return d


def _ntt(a, sign, mod, g):
        n = len(a)
        tmp = (mod - 1) * modinv(n, mod) % mod  # -1/n
        h = pow(g, tmp, mod)  # ^n√g
        if sign < 0:
            h = modinv(h, mod)

        a = bit_reverse(a)

        m = 1
        while m < n:
            m2 = m << 1
            _base = pow(h, n // m2, mod)
            _w = 1
            for x in range(m):
                for s in range(x, n, m2):
                    u = a[s]
                    d = a[s + m] * _w % mod
                    a[s] = (u + d) % mod
                    a[s + m] = (u - d) % mod
                _w = _w * _base % mod
            m <<= 1
        return a

def ntt(a, mod, g):
        return _ntt(a, 1, mod, g)
  
def intt(a, mod, g):
        n = len(a)
        n_inv = modinv(n, mod)
        a = _ntt(a, -1, mod, g)
        for i in range(n):
            a[i] = a[i] * n_inv % mod
        return a
      
def convolution(a, b, mod, g):
        ret_size = len(a) + len(b) - 1
        n = 1 << (ret_size - 1).bit_length()
        _a = a + [0] * (n - len(a))
        _b = b + [0] * (n - len(b))
        _a = ntt(_a, mod, g)
        _b = ntt(_b, mod, g)
        _a = [x * y % mod for x, y in zip(_a, _b)]
        _a = intt(_a, mod, g)
        _a = _a[:ret_size]
        return _a


def convolution_ntt(a, b, mod):
    a = [x % mod for x in a]
    b = [x % mod for x in b]

    mods = (167772161, 469762049, 1224736769, mod)

    ntt1 = NTT(mods[0], 3)
    ntt2 = NTT(mods[1], 3)
    ntt3 = NTT(mods[2], 3)

    x1 = ntt1.convolution(a, b)
    x2 = ntt2.convolution(a, b)
    x3 = ntt3.convolution(a, b)

    n = len(x1)
    ret = [0] * n
    for i in range(n):
        xs = [x1[i], x2[i], x3[i], 0]
        ret[i] = _garner(xs, mods)

    return ret

N = 100000
A = []
B = []
s = 0
for i in range(N):
    s = (s * 3 + i * 7) % 100
    a = s
    b = (s * 3 + a * 11) % 100
    A.append(a)
    B.append(b)

AB = convolution(A, B, 998244353, 5)


#####
A, B, C, K = map(int, input().split())
if K <= A + B:
    print(min(A, K))
else:
    print(A - (K - A - B))
