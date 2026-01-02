from functools import reduce

n = int(input())
a = list(map(int, input().split()))

m = max(a)
d = [0] * (m + 1)
d[1] = 1
for i in range(2, m + 1):
    for j in range(i, m + 1, i):
        if d[j] == 0:
            d[j] = i

def prime_factorize(n):
    res = []
    if n == 1:
        return res
    while n > 1:
        res.append(d[n])
        n //= d[n]
    return res

def is_pairwise_coprime():
    exists = [0] * (m + 1)
    for ai in a:
        for p in set(prime_factorize(ai)):
            if exists[p]:
                return False
            exists[p] = 1
    return True

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def is_setwise_coprime():
    return reduce(gcd, a) == 1


if is_pairwise_coprime():
    print('pairwise coprime')
elif is_setwise_coprime():
    print('setwise coprime')
else:
    print('not coprime')