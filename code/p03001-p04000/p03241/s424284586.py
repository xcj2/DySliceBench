from math import floor, ceil, sqrt
N, M = [int(elem) for elem in input().split(' ')]

def factorize(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


def divisorize(fct):
    try:
        b, e = fct.pop()  # base, exponent
    except:
        return []
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]


def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

M_divisors = divisorize(factorize(M))
threshold = M // N
max_possible_divisor = 1
for M_divisor in M_divisors:
    divisor = num(M_divisor)
    if divisor <= threshold:
        max_possible_divisor = max(max_possible_divisor, divisor)
print(max_possible_divisor)
