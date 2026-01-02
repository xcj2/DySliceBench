def crt(R, M):
    def exEuclid(a, mod):
        b = mod
        s, u = 1, 0
        while b:
            q = a // b
            a, b = b, a % b
            s, u = u, s - q * u
        return a, s % mod
    assert len(R) == len(M)
    r0, m0 = 0, 1
    for r, m in zip(R, M):
        assert m >= 1
        r %= m
        if m0 < m:
            r0, r = r, r0
            m0, m = m, m0
        if m0 % m == 0:
            if r0 % m != r:
                return (0, 0)
            continue
        g, im = exEuclid(m0, m)
        u = m // g
        if (r - r0) % g:
            return (0, 0)
        x = (r - r0) // g % u * im % u
        r0 += x * m0
        m0 *= u
        if r0 < 0:
            r0 += m0
    return (r0, m0)


def atcoder_acl1_b():
    N = int(input())
    def divisor(n):
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                yield i
                if i != n // i:
                    yield n // i

    ans = 10**20
    for x in divisor(2*N):
        kc, _ = crt([0, -1], (x, 2*N//x))
        if kc != 0:
            ans = min(ans, kc)
    print(ans)


if __name__ == '__main__':
    atcoder_acl1_b()
