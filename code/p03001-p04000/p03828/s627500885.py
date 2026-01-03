import math

N = int(input())

class remainder():
    def __init__(self, mod=(10**9 + 7)):
        self.mod = mod
    
    def mul(self, a, b):
        return ((a % self.mod) * (b % self.mod)) % self.mod

    def pow(self, a, b):
        bp = []
        #bp.append(1)
        bp.append(a)

        n = len(bin(b)) - 2
        for x in range(n):
            bp.append(bp[x]**2 % self.mod)

        res = 1
        for x in range(n):
            if b >> x & 1:
                res = (res * bp[x]) % self.mod
        
        return res

    def div(self, a, b):
        
        return self.mul(a, self.pow(b, self.mod - 2))


def findAllOfPrime(N):
    prime = [True] * (N + 1)
    prime[0] = False
    prime[1] = False

    x = 2
    while x**2 <= N:
        if prime[x]:
            j = 2
            while x * j <= N:
                prime[x * j] = False
                j += 1
        x += 1

    return prime

re = remainder()
primes = set()
for n in range(1, N + 1):
    prime = findAllOfPrime(n)
    for i, p in enumerate(prime):
        if p:
            primes.add(i)

A = math.factorial(N)
ans = 1
for p in primes:
    cnt = 1
    while A % p == 0:
        cnt += 1
        A //= p
    ans = re.mul(ans, cnt)
print(ans)


