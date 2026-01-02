import sys


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_prime_MR(n):
    d = n - 1
    d = d // (d & -d)
    L = [2, 7, 61] if n < 1 << 32 else [
        2, 3, 5, 7, 11, 13, 17
    ] if n < 1 << 48 else [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in L:
        t = d
        y = pow(a, t, n)
        if y == 1:
            continue
        while y != n - 1:
            y = y * y % n
            if y == 1 or t == n - 1:
                return 0
            t <<= 1
    return 1


def find_factor_rho(n):
    m = 1 << n.bit_length() // 8
    for c in range(1, 99):

        def f(x):
            return (x * x + c) % n

        y, r, q, g = 2, 1, 1, 1
        while g == 1:
            x = y
            for i in range(r):
                y = f(y)
            k = 0
            while k < r and g == 1:
                ys = y
                for i in range(min(m, r - k)):
                    y = f(y)
                    q = q * abs(x - y) % n
                g = gcd(q, n)
                k += m
            r <<= 1
        if g == n:
            g = 1
            while g == 1:
                ys = f(ys)
                g = gcd(abs(x - ys), n)
        if g < n:
            if is_prime_MR(g):
                return g
            elif is_prime_MR(n // g):
                return n // g
            return find_factor_rho(g)


def prime_factor(n):
    i = 2
    ret = {}
    rhoFlg = 0
    while i * i <= n:
        k = 0
        while n % i == 0:
            n //= i
            k += 1
        if k:
            ret[i] = k
        i += i % 2 + (3 if i % 3 == 1 else 1)
        if i == 101 and n >= 2**20:
            while n > 1:
                if is_prime_MR(n):
                    ret[n], n = 1, 1
                else:
                    rhoFlg = 1
                    j = find_factor_rho(n)
                    k = 0
                    while n % j == 0:
                        n //= j
                        k += 1
                    ret[j] = k
    if n > 1:
        ret[n] = 1
    if rhoFlg:
        ret = {x: ret[x] for x in sorted(ret)}
    return ret


input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
g = 0
for a in A:
    g = gcd(g, a)

if g > 1:
    print('not coprime')
    exit()

X = [0] * 1001001
for a in A:
    for p in prime_factor(a):
        if X[p]:
            print('setwise coprime')
            exit()
        X[p] = 1

print('pairwise coprime')
