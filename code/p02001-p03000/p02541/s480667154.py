def inv_gcd(a, b):
    a %= b
    if a == 0:
        return (b, 0)
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

    if m0 < 0:
        m0 += b // s

    return (s, m0)

def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0 = 0
    m0 = 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue
        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g:
            return (0, 0)
        x = (r1 - r0) // g % u1 * im % u1
        r0 += x * m0
        m0 *= u1  # -> lcm(m0, m1)
        if r0 < 0:
            r0 += m0

    return (r0, m0)

def prime_de(number):
    factor = []
    div = 2
    while div*div <= number:
        cnt = 0
        while number % div == 0:
            cnt += 1
            number //= div
        if cnt != 0:
            factor.append((div, cnt))
        div += 1
    if number > 1:
        factor.append((number, 1))
    return factor

N, = map(int, input().split())
p = prime_de(N)
lp = len(p)
R = 10**18
for i in range(2**lp):
    l = []
    for j in range(lp):
        i, m = divmod(i, 2)
        l.append(m)
    r, m = [], []
    for j in range(lp):
        a, b = p[j]
        c = a**b if a!=2 else a**(b+1)
        if l[j]:
            r.append(0)
        else:
            r.append(c-1)
        m.append(c)
    x, y = crt(r, m)
    if x:
        R = min(R, x)
    else:
        R = min(R, y)
print(R)

