def sieve_of_eratosthenes(N):
    N += 1
    sieve = [0] * N
    for p in range(2, N):
        if sieve[p]:
            continue
        for i in range(p, N, p):
            sieve[i] = p
    return sieve

def lcm_with_sieve(numbers, N):
    sieve = sieve_of_eratosthenes(N)
    lcm = dict()
    for n in numbers:
        d = dict()
        while n > 1:
            factor = sieve[n]
            n //= factor
            d[factor] = d.get(factor, 0) + 1
        for factor, power in d.items():
            lcm[factor] = max(lcm.get(factor, 0), power)
    return lcm

def main():
    MOD = 10 ** 9 + 7
    _, *A = map(int, open(0).read().split())
    lcm = 1
    for factor, power in lcm_with_sieve(A, 10 ** 6).items():
        lcm = lcm * pow(factor, power, MOD) % MOD
    total = 0
    for a in A:
        total = (total + lcm * pow(a, MOD - 2, MOD)) % MOD
    print(total)

main()