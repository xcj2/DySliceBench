import math

def cmb(n, r,MOD=10**9+7):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n;
 
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
 
    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
 
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k]) % MOD
 
    return result % MOD

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

from collections import Counter
def main():
    n,m  = map(int,input().split())
    c = Counter(prime_factorize(m))
    ans = 1
    for i in c.values():
        ans *= cmb(n+i-1,i)
        ans %= 10**9+7
    print(ans%(10**9+7))
if __name__ == '__main__':
    main()