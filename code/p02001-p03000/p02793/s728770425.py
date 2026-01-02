import collections
import sys

input = sys.stdin.readline

ri = lambda: int(input())
rs = lambda: input().rstrip()
ril = lambda: list(map(int, input().split()))
rsl = lambda: input().rstrip().split()
ris = lambda n: [ri() for _ in range(n)]
rss = lambda n: [rs() for _ in range(n)]
rils = lambda n: [ril() for _ in range(n)]
rsls = lambda n: [rsl() for _ in range(n)]


def eratosthenes(n):
    sieve = [True for _ in range(n + 1)]
    sieve[0] = False
    sieve[1] = False

    def _update(p):
        if sieve[p]:
            for i in range(p * 2, n + 1, p):
                sieve[i] = False

    if n > 1:
        _update(2)
    p = 3
    while p * p <= n:
        _update(p)
        p += 2
    return sieve


def factorize(n, primes):
    import collections
    if n < 2:
        return dict()
    counter = collections.Counter()
    for p in primes:
        while n % p == 0:
            counter[p] += 1
            n //= p
        if n == 1:
            break
    if n > 1:
        counter[n] += 1
    return counter


MOD = 10**9 + 7

n = ri()
ls = ril()
if n == 1:
    print(1)
    exit()

sieve = eratosthenes(10**3)
primes = [x for x, b in enumerate(sieve) if b]

lcm_counter = collections.Counter()
for x in ls:
    counter = factorize(x, primes)
    for p, k in counter.items():
        lcm_counter[p] = max(lcm_counter[p], k)
lcm = 1
for p, k in lcm_counter.items():
    lcm *= pow(p, k, MOD)
    lcm %= MOD

res = 0
for x in ls:
    res += lcm * pow(x, MOD - 2, MOD)
    res %= MOD
print(res)