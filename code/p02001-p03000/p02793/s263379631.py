class PrimeOptimizer:
    def __init__(self, MAX_NUM=10**3):
        is_prime = [True] * MAX_NUM
        is_prime[0] = False
        is_prime[1] = False
        primes = []
        for i in range(MAX_NUM):
            if is_prime[i]:
                primes.append(i)
                for j in range(2*i, MAX_NUM, i):
                    is_prime[j] = False
        self.primes = primes

    def prime_factorization(self, x):
        res = {}
        for prime in self.primes:
            while x % prime == 0:
                if not prime in res:
                    res[prime] = 0
                res[prime] += 1
                x //= prime
        if x > 1:
            res[x] = 1
        return res

MOD = 10**9+7

def mod_pow(p, q):
    res = 1
    while q:
        if q & 1:
            res = (res * p) % MOD
        p = (p * p) % MOD
        q //= 2
    return res

def mod_inv(p):
    return mod_pow(p, MOD - 2)

def solve(n, a):
    primeOpt = PrimeOptimizer()
    D = {}
    for i in range(n):
        prime_num_mapping = primeOpt.prime_factorization(a[i])
        for prime, num in prime_num_mapping.items():
            if not prime in D:
                D[prime] = 0
            D[prime] = max(D[prime], num)
    L = 1
    for prime, num in D.items():
        L = (L * mod_pow(prime, num)) % MOD
    res = sum([L * mod_inv(x) % MOD for x in a])
    return res % MOD

N = int(input())
A = list(map(int, input().split()))
print(solve(N, A))