N, K = map(int, input().split())


class MathUtil:
    # calculate {m+n}C{n}
    def egcd(self, a: int, b: int):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a: int, m: int):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def combination(self, n: int, r: int, mod: int = 10**9+7) -> int:
        r = min(r, n-r)
        res = 1
        for i in range(r):
            res = res * (n-i) * self.modinv(i+1, mod) % mod
        return res


m = 10**9+7
for i in range(1, K+1):
    a = MathUtil().combination(K-1, i-1, m)
    if N-K+1 >= i:
        b = MathUtil().combination(N-K+1, i, m)
    else:
        b = 0
    print((a*b) % m)
