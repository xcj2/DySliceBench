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
def main():
    H, W, A, B = map(int, input().split())
    mod = 10**9 + 7
    c = cmbs(mod)
    r = c.cmb(H+W-2, H-1)
    for i in range(1, B+1):
        r -= c.cmb(H-A+i-2, i-1) * c.cmb(A-1+W-i, A-1)
    return r % mod
print(main())
