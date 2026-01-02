N, M = map(int, input().split())

def primefactorize(n):
    fct = []  # return [[p1, power1], [p2, power2], ...]
    p, power = 2, 0
    while p * p <= n:
        while n % p == 0:
            n = n // p
            power += 1
        if power > 0:
            fct.append([p, power])
        if p == 2:
            p += 1
        else:
            p += 2
        power = 0
    if n > 1:
        fct.append([n, 1])
    return fct

def divisorize(fct):
    b, e = fct.pop()  # base, exponent
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b, k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]

def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base**exponent
    return a

if M != 1:
    fct = primefactorize(M)
    factors = []
    for div in divisorize(fct):
        factors.append(num(div))
else:
    factors = [1]
factors.sort()
k = M//N
L = [x for x in factors if x <= k]
print(max(L))