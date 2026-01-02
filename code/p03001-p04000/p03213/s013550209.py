import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)

def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


from collections import Counter


def factorize(n: int):
    d = Counter()
    m = 2

    while m * m <= n:
        while n % m == 0:
            n //= m
            d[m] += 1

        m += 1

    if n > 1:
        d[n] += 1

    return d


n = ni()
prime_counter = Counter()

for i in range(2, n+1):
    primes = factorize(i)
    prime_counter += primes

# カウント
gteq74 = 0
gteq24 = 0
gteq14 = 0
gteq4 = 0
gteq2 = 0
gteq2_and_lt4 = 0
for _, cnt in prime_counter.items():
    gteq74 += 1 if cnt >= 74 else 0
    gteq24 += 1 if cnt >= 24 else 0
    gteq14 += 1 if cnt >= 14 else 0
    gteq4 += 1 if cnt >= 4 else 0
    gteq2 += 1 if cnt >= 2 else 0
    gteq2_and_lt4 += 1 if 2 <= cnt < 4 else 0

ans = gteq74 + (gteq24*gteq2 - gteq24) + (gteq14*gteq4 - gteq14)
ans += gteq4 * (gteq4-1) * (gteq4-2) // 2 + gteq4 * (gteq4-1) * gteq2_and_lt4 // 2

print(ans)
