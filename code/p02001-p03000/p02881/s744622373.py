from collections import defaultdict


def factorize(n):
    f = defaultdict(int)
    tmp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        while tmp % i == 0:
            f[i] += 1
            tmp //= i
    if tmp != 1:
        f[tmp] += 1
    if not f:
        f[n] += 1
    return f


def distance(s, d):
    a, b = 1, 1
    for i, si in enumerate(s):
        if si == "0":
            a *= factors[i]
            if a > d:
                return inf
        else:
            b *= factors[i]
            if b > d:
                return inf
    return a + b - 2


def answer(f, d):
    a = 1
    for i in f:
        a *= i
        if a > d:
            return inf
    return a + N // a - 2


def sa(f):
    d = inf
    for fi in f:
        d = min(d, answer(fi, d))
    return d


def comb(f):
    c = [[]]
    for k in f:
        ct = [[k] * i for i in range(1, f[k] + 1)]
        ci = c.copy()
        for cti in ct:
            for cii in ci:
                c.append(cii + cti)
    return [[1]] + c[1:]


# CONST = 1099511627776
N = int(input())
inf = 999999999999
factors = factorize(N)
print(sa(comb(factors)))