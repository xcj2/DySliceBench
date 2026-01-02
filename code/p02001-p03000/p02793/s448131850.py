import sys
sys.setrecursionlimit(100000000)
import collections
import math

MOD = 10**9 + 7
n = int(input())
a = list(map(int, input().split()))


def eratosthenes(n):  #エラトステネスの篩
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


def factorize(n, primes):        # 素数の値をカウントする
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


if n == 1:
    print(1)
    exit()

sieve = eratosthenes(10 ** 3)
primes = [x for x, b in enumerate(sieve) if b]

lcm = collections.Counter()
for x in a:
    counter = factorize(x, primes)
    for p, k in counter.items():
        lcm[p] = max(lcm[p], k)
lcm_val = 1
for p, k in lcm.items():  # 各素因数と個数
    lcm_val *= pow(p, k, MOD)
    #lcm_val %= MOD       # 最小公倍数


res = 0
for x in a:
    res += lcm_val * pow(x, MOD - 2, MOD)  # 最小公倍数lcm_val / 各値x の余り 逆元をとる
    res %= MOD
print(res)