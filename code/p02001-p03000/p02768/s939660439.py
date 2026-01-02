n, a, b = map(int, input().split())

MOD = 10 ** 9 + 7

class Factorial:
    def __init__(self, n, mod):
        self.f = [1]
        self.mod = mod
        for j in range(1, n + 1):
            self.f.append(self.f[-1] * j % mod)
        self.i = [pow(self.f[-1], mod - 2, mod)]
        for j in range(n, 0, -1):
            self.i.append(self.i[-1] * j % mod)
        self.i.reverse()
    def factorial(self, j):
        return self.f[j]
    def ifactorial(self, j):
        return self.i[j]
    def comb(self, n, k):
        return self.f[n] * self.i[n - k] % self.mod * self.i[k] % self.mod if n >= k else 0

c = Factorial(max(a, b) + 1, MOD)

def combination(n, r): #nCrを求める
    if n - r < r:
        r = n - r
    tmp = 1
    for i in range(n - r + 1, n + 1):
        tmp *= i
        tmp %= MOD
    tmp *= c.ifactorial(r)
    return tmp

MOD = 10 ** 9 + 7


ans = pow(2, n, MOD) - 1 #選ばないのを除く

ans -= combination(n, a)
ans %= MOD
ans -= combination(n, b)
ans %= MOD

print (ans)