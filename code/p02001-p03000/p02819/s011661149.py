x = int(input())

# 自然数m以下の素数を返す
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def prime_numbers_under(m):
    # 素数を保持するset
    primes = set()

    # 2以上m以下の素数を数え上げる
    n = 2
    while n <= m:
        # 自身より小さい全ての素数で割り切れなければ、素数とみなせる
        if all(n % i != 0 for i in primes):
            primes.add(n)
        n += 1

    return primes

# 自然数m以上の素数を返す
def prime_numbers_over(m):
    # 素数を保持するset
    # primes = set()
    global p

    if m in p:
        return m

    while True:
        # 自身より小さい全ての素数で割り切れなければ、素数とみなせる
        if all(m % i != 0 for i in p):
            return m
        m += 1

# p = prime_numbers_under(x)
p = primes(x)

print(prime_numbers_over(x))