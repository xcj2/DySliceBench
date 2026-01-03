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
    N = int(input())
    A = list(map(int, input().split()))
    d = {}
    dif = 0
    for i, v in enumerate(A):
        if v not in d:
            d[v] = i
        else:
            dif = i - d[v]
            break
    mod = 10**9 + 7
    c = cmbs(mod)
    print(N)
    if N == 1:
        print(N)
        return
    if dif == 1:
        for i in range(2, N):
            if N-1 >= i:
                r = c.cmb(N-1, i-2) + c.cmb(N-1, i-1) + c.cmb(N-1, i)
            else:
                r = c.cmb(N-1, i-2) + c.cmb(N-1, i-1)
            print(r % mod)
        print(N)
        print(1)
        return
    for i in range(2, N):
        r = c.cmb(N-1, i-2) + c.cmb(N-1, i-1)*2 - c.cmb(N-dif, i-1) + c.cmb(N-1, i)
        print(r % mod)
    print(N+1)
    print(1)
main()
