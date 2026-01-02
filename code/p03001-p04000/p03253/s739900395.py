class cmbs(object):
    def __init__(self, mod):
        self.mod = mod
        self.g1 = [1, 1]
        self.g2 = [1, 1]
        inverse = [0, 1]
        for i in range(2, 10 ** 6 + 1):
            self.g1.append((self.g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod // i)) % mod)
            self.g2.append((self.g2[-1] * inverse[-1]) % mod)

    def cmb(self, n, r):
        if n > 10 ** 6:
            return self.cmbl(n, r)
        return self.cmbr(n, r)

    def cmbr(self, n, r):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return self.g1[n] * self.g2[r] * self.g2[n-r] % self.mod

    def cmbl(self, n, r):
        t = 1
        r = min(r, n-r)
        for i in range(n - r + 1, n + 1):
            t = t * i % self.mod
        return t * self.g2[r] % self.mod
def prime_factorize(n):
    a = {}
    while n % 2 == 0:
        if 2 in a:
            a[2] += 1
        else:
            a[2] = 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f in a:
                a[f] += 1
            else:
                a[f] = 1
            n //= f
        else:
            f += 2
    if n != 1:
        if n in a:
            a[n] += 1
        else:
            a[n] = 1
    return a
def main():
    N, M = map(int, input().split())
    d = prime_factorize(M)
    MOD = 10**9 + 7
    c = cmbs(MOD)
    r = 1
    for i in d:
        r *= c.cmb(N+d[i]-1, N-1)
    r %= MOD
    print(r)
main()
