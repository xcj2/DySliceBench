class Combinations:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod # mod must be prime
        self.prepare()

    def prepare(self):
        self.factorialNumInverse = [None] * (n + 1)
        self.naturalNumInverse = [None] * (n + 1)
        self.fact = [None] * (n + 1)
        self.inverseOfNumber()
        self.inverseOfFactorial()
        self.factorial()

    def inverseOfNumber(self):
        self.naturalNumInverse[0] = self.naturalNumInverse[1] = 1
        for i in range(2, n + 1):
            self.naturalNumInverse[i] = (self.naturalNumInverse[self.mod % i] * (self.mod - self.mod // i) % self.mod)

    def inverseOfFactorial(self):
        self.factorialNumInverse[0] = self.factorialNumInverse[1] = 1
        for i in range(2, n + 1):
            self.factorialNumInverse[i] = (self.naturalNumInverse[i] * self.factorialNumInverse[i - 1]) % self.mod

    def factorial(self):
        self.fact[0] = 1
        for i in range(1, n + 1):
            self.fact[i] = (self.fact[i - 1] * i) % self.mod

    def nCk(self, n, k):
        ans = ((self.fact[n] * self.factorialNumInverse[k]) % self.mod * self.factorialNumInverse[n - k]) % self.mod
        return ans

MOD = 10 ** 9 + 7

n, k = map(int, input().split())
a = sorted(map(int, input().split()))

combs = Combinations(n, MOD)

def calcSum(a):
    ret = 0
    for i in range(k - 1, n):
        ret += (combs.nCk(i, k - 1) * a[i]) % MOD
        ret %= MOD
    return ret

print((calcSum(a) - calcSum(a[::-1])) % MOD)