from collections import defaultdict


def prime_factorize(n):
    i = 2
    res = defaultdict(lambda: 0)
    while i * i <= n:
        while n % i == 0:
            res[i] += 1
            n = n // i
        i += 1
    if n != 1:
        res[n] = 1
    res = dict(res)
    return res


def divisor(n):
    i = 1
    res = set()
    while i * i <= n:
        if n % i == 0:
            res.add(i)
            res.add(n // i)
        i += 1
    return res


def solve(n):
    pf1 = prime_factorize(n - 1)
    ans = 1
    for v in pf1.values():
        ans *= v + 1
    ans -= 1
    # print(ans)

    pf2 = divisor(n)
    pf2.remove(1)
    for y in pf2:
        m = n
        while m % y == 0:
            m //= y
        m %= y
        if m == 1:
            ans += 1
    return ans


n = int(input())
print(solve(n))
