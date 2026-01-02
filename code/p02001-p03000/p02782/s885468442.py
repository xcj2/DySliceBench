from collections import defaultdict

class ModInt:

    def __init__(self, mod=1000000007, mem_size=3000000):
        self.mod = mod
        self.mem_factorial = [0] * mem_size
        self.mem_size = mem_size
        self.mem_inv = [0] * mem_size
        self.mem_invfactorial = [0] * mem_size
        self.mem_factorial[0] = 1
        self.mem_inv[1] = 1
        self.mem_invfactorial[0] = 1
        for i in range(1, mem_size):
            self.mem_factorial[i] = self.mem_factorial[i-1]*i % mod
            if i > 1:
                self.mem_inv[i] = (-1) * (mod//i) * (self.mem_inv[mod % i]) % mod
            self.mem_invfactorial[i] = self.mem_invfactorial[i-1] * self.mem_inv[i] % mod

    def inverse(self, x):
        if x < self.mem_size:
            return self.mem_inv[x]
        mod = self.mod
        return int(pow(x, mod-2, mod))

    def factorial(self, x):
        return self.mem_factorial[x]

    def invfactorial(self, x):
        return self.mem_invfactorial[x]


    def comb(self, m, n):
        mod = self.mod
        a = self.factorial(m)
        b = self.invfactorial(n)
        c = self.invfactorial(m - n)
        ret = a * b * c % mod
        return ret

mod = 1000000007

modint = ModInt(mod)


def r_sum(r, c):
    a = modint.factorial(c + r + 1) * (r + 1)
    b = modint.invfactorial(c + 1) * modint.invfactorial(r + 1)
    ret = a * b
    return ret % mod


def F(r, c):
    ret = 0
    for i in range(c + 1):
        ret += r_sum(r, i)
    return ret % mod

r_from, c_from, r_to, c_to = map(int, input().split())

ans = F(r_to, c_to)
ans -= F(r_to, c_from - 1)
ans -= F(r_from - 1, c_to)
ans += F(r_from - 1, c_from - 1)
ans %= mod

print(ans)
