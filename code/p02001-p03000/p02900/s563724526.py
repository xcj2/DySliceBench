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

def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)


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

from collections import Counter

a, b = li()

g = gcd(a, b)
f = factorize(g)

print(len(f) + 1)