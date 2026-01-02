from collections import defaultdict


def read():
    N = int(input())
    return N,


def sieve(n):
    """
    n以下の素数を昇順に列挙する
    """
    is_prime = [True for i in range(n+1)]
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i+i, n+1, i):
                is_prime[j] = False
    return primes


def prime_factorization(n, primes):
    """
    nの素因数分解を求める
    """
    prime_factors = defaultdict(int)
    if n < 2:
        return prime_factors
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            prime_factors[p] += 1
            n //= p
    if n > 1:
        prime_factors[n] = 1
    return prime_factors


def divisor(n, primes):
    d = []
    for i in range(1, n+1):
        if i * i > n:
            break
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
    return list(sorted(d))


def solve(N):
    primes = sieve(N)
    factors = defaultdict(int)
    for x in range(1, N+1):
        pf = prime_factorization(x, primes)
        for p, v in pf.items():
            factors[p] += v
    V = [v for v in factors.values()]
    
    c = defaultdict(int)
    for v in V:
        for x in [3, 5, 15, 25, 75]:
            if v+1 >= x:
                c[x] += 1
    count = 0
    # (75) 
    count += c[75]
    # (25, 3)
    count += c[25] * (c[3]-1)
    # (15, 5)
    count += c[15] * (c[5]-1)
    # (5, 5, 3)
    count += (c[5] * (c[5]-1) // 2) * (c[3]-2)

    return count

if __name__ == '__main__':
    inputs = read()
    print("%s" % solve(*inputs))
