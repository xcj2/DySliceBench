class Factorial:
    def __init__(self, n, mod=10**9+7):
        self.fac = [0] * (n+1)
        self.ifac = [0] * (n+1)
        self.fac[0] = 1
        self.ifac[0] = 1
        modmod = mod - 2
        for i in range(n):
            self.fac[i+1] = self.fac[i] * (i+1) % mod
            self.ifac[i+1] = self.ifac[i] * pow(i+1, modmod, mod) % mod

    def comb(self, n, r):
        if n == 0 and r == 0:
            return 1
        if n < r or n < 0:
            return 0
        tmp =  self.ifac[n-r] * self.ifac[r] % mod
        return tmp * self.fac[n] % mod

    def perm(self, n, r):
        if n == 0 and r == 0:
            return 1
        if n < r or n < 0:
            return 0
        return (self.fac[n] * self.ifac[n-r]) % mod

def make_divisors(n):
    divisors = {}
    tmp = n
    for div in range(2, int(n**0.5)+1):
        if n % div == 0:
            divisors[div] = 0
        while n % div == 0:
            n //= div
            divisors[div] += 1
        div += 1
    if n > 1:
        divisors[n] = 1
    return divisors

n,m = map(int, input().split())
mod = 10**9 + 7
divisors = make_divisors(m)
fact = Factorial(n + sum(divisors.values()) + 1)

ans = 1
for value in divisors.values():
    ans = ans * fact.comb(value+n-1,value) % mod
print(ans)
