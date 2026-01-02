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


x, y = map(int, input().split())


m = - x + 2*y
n = 2*x - y

if m % 3 != 0 or n % 3 != 0 or m < 0 or n < 0:
    print(0)
else:
    m //= 3
    n //= 3

    print(MathUtil().combination(m+n, n))
