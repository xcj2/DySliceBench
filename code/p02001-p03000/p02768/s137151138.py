class cmbs(object):
    def __init__(self, mod):
        self.mod = mod
        self.g1 = [1, 1]
        # g2[i] ha i no kaijo no gyakugen
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
        mod = self.mod
        for i in range(n - r + 1, n + 1):
            t = t * i % mod
        return t * self.g2[r] % mod
def pown(n, m, mod):
    r = 1
    while n:
        if n & 1:
            r = r * m
            r %= mod
        m *= m
        m %= mod
        n >>= 1
    return r

def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    c = cmbs(mod)
    return (pown(n, 2, mod) - 1 - c.cmb(n, a) - c.cmb(n, b)) % mod
print(main())

