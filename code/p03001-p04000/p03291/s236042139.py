from functools import lru_cache
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
    @lru_cache(maxsize=None)
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
    S = input()
    mod = 10**9 + 7
    n = len(S)
    A = [0] * n
    B = [0] * n
    C = [0] * n
    Q = [0] * n
    d = {'A':0, 'B':0, 'C':0, '?':0}
    for i, v in enumerate(S):
        d[v] += 1
        A[i] = d['A']
        B[i] = d['B']
        C[i] = d['C']
        Q[i] = d['?']
    r = 0
    c = cmbs(mod)
    t = d['?']
    # ???
    if t >= 3:
        r += c.cmb(t, 3) * pow(3, t - 3)
        r %= mod
    if t >= 2:
        r2 = 0
        for i in range(n):
            p = t - Q[i]
            # A??
            if S[i] == 'A' and p >= 2:
                r2 += c.cmb(p, 2)
            # ?B?
            if S[i] == 'B' and Q[i] >= 1 and p >= 1:
                r2 += Q[i] * p
            # ??C
            if S[i] == 'C' and Q[i] >= 2:
                r2 += c.cmb(Q[i], 2)
        r2 *= pow(3, t-2)
        r += r2
        r %= mod
    if t >= 1:
        r1 = 0
        for i in range(n):
            if S[i] == 'B':
                #AB?
                r1 += A[i] * (t - Q[i])
                #?BC
                r1 += Q[i] * (d['C']-C[i])
            if S[i] == '?':
                #A?C
                r1 += A[i] * (d['C']-C[i])
        r1 *=  pow(3, t-1)
        r += r1
        r %= mod
    r0 = 0
    for i in range(n):
        if S[i] == 'B':
            r0 += A[i] * (d['C'] - C[i])
    r0 *= pow(3, t)
    r += r0
    r %= mod
    return r
print(main())
