import collections
from operator import mul
from functools import reduce

def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def main():
    N, M = map(int, input().split())

    MOD = 10 ** 9 + 7
    c = collections.Counter(prime_factorize(M))
    ans = 1
    for i, j in c.items():
        ans *= cmb(N+j-1,N-1)
        ans %= MOD

    print(ans)

main()