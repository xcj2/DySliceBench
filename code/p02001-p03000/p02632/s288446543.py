class cmbs(object):
    def __init__(self, mod):
        self.mod = mod
        self.g1 = [1, 1]
        self.g2 = [1, 1]
        inverse = [0, 1]
        for i in range(2, 2 * (10 ** 6) + 1):
            self.g1.append((self.g1[-1] * i) % mod)
            inverse.append((-inverse[mod % i] * (mod // i)) % mod)
            self.g2.append((self.g2[-1] * inverse[-1]) % mod)

    def cmb(self, n, r):
        if n > 2 * (10 ** 6):
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
def main():
    K = int(input())
    S = input()
    l = len(S)
    mod = 10**9 + 7
    c = cmbs(mod)
    r = 0
    x25 = 1
    x26 = pow(26, K, mod)
    inv26 = pow(26, mod-2, mod)
    for i in range(K+1):
        r = (r + c.cmb(l+i-1, i) * x25 * x26) % mod
        x25 = x25 * 25 % mod
        x26 = x26 * inv26 % mod
    return r % mod
print(main())
