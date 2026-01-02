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

    def pow(self, x: int, n:int, mod: int = 10**9+7):
        if n == 0:
            return 1

        k = 1
        while n > 1:
            if n % 2 != 0:
                k *= x
            
            x *= x
            n //= 2

            if k >= mod:
                k %= mod
            if x >= mod:
                x %= mod

        return (k * x) % mod 

util = MathUtil()

n, a, b = map(int, input().split())

m = 10**9 + 7

if n >= a:
    ca = util.combination(n,a)
else:
    ca = 0

if n >= b :
    cb = util.combination(n,b)
else:
    cb = 0

print( (2 * m + util.pow(2, n) -1 - ca - cb) % m)