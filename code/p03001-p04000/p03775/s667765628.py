MAX_PRIME = 10**5 + 10
is_prime = [1] * MAX_PRIME
primes = []
is_prime[0] = 0
is_prime[1] = 0
for i in range(MAX_PRIME):
    if is_prime[i]:
        primes.append(i)
        for j in range(2, ((MAX_PRIME-1)//i) + 1):
            is_prime[i*j] = 0

def factorization(n):
    factor = {}
    for p in primes:
        if p ** 2 > n:
            break
        while n % p == 0:
            n //= p
            if p not in factor:
                factor[p] = 1
            else:
                factor[p] += 1
    if n > 1:
        factor[n] = 1
    return factor

n = int(input())

f = factorization(n)

def F(a, b):
    return max(len(str(a)), len(str(b)))

k = sorted(list(f.keys()))
def dfs(num, i):
    if i < len(k):
        m = 10 ** 18
        p = k[i]
        for j in range(f[p]+1):
            m = min(m, dfs(num * p ** j, i+1))
        return m
    return F(num, n // num)

print(dfs(1, 0))