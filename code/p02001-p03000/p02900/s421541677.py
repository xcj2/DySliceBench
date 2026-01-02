import sys
input=sys.stdin.readline

import fractions
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

import math
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

import collections
def main():
    A,B = map(int, input().split())

    da = make_divisors(A)
    db = make_divisors(B)
    cds = set(da) & set (db)
    P = prime_factorize(max(cds))
    P.append(1)
    c = collections.Counter(P).keys()
    x = cds & set(c)
    print(len(x))


if __name__ == '__main__':
    main()
