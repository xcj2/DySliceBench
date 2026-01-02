N, M = [int(_) for _ in input().split()]

MOD = 10**9+7

def primes(n):
    from math import sqrt
    mn = int(sqrt(n)) + 2
    p = [1] * mn
    for x in range(2, mn):
        if p[x]:
            y = x * x
            while y < mn:
                p[y] = 0
                y += x
    return (i for i in range(2, mn) if p[i])

def calc(M):
    result = {}
    for n in primes(M):
        if M % n == 0:
            result[n] = 1
            M //= n
        while M % n == 0:
            result[n] += 1
            M //= n
    if M > 1:
        result[M] = 1
    return result

def C(x, y):
    n = min(y, x - y)
    r = 1
    for i in range(n):
        r = r * (x - i)
    for i in range(n):
        r = r // (i + 1)
    return r

cs = calc(M)

result = 1

for x in cs.values():
    result = result * C(N+x-1, N-1) % MOD

print(result)
