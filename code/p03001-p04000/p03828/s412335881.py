def divisor(n):
    if n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    maxitr = intSqrt(n)
    i = 1
    while True:
        i += 4
        if i > maxitr:
            return n
        elif n % i == 0:
            return i
        i += 2
        if i > maxitr:
            return n
        elif n % i == 0:
            return i


def factorization(n, simple=True):
    result = []
    while n > 1:
        div = divisor(n)
        result.append(div)
        n //= div
    return result


def intSqrt(n):
    x = 1
    while True:
        x2 = (x + n // x) // 2
        if abs(x - x2) <= 1:
            break
        x = x2
    return x2


def ABC052C(n):
    factor = []
    for i in range(2, n+1):
        factor.extend(factorization(i))
    # index, counts = sp.unique(factor, return_counts=True)
    d = {}
    for c in factor:
        if c in d.keys():
            d[c] += 1
        else:
            d.setdefault(c, 1)
    ans = 1
    for key, value in d.items():
        ans = (ans * (value + 1)) % 1000000007
    print(ans)

ABC052C(int(input()))
