import math


def get_primes(n):
    primes = []
    checks = [True for _ in range(int(math.sqrt(n)) + 1)]
    checks[0] = checks[1] = False
    for i in range(2, len(checks)):
        if checks[i]:
            primes.append(i)
            tmp = 0
            while i + tmp * i < len(checks):
                checks[i + tmp * i] = False
                tmp += 1
    return primes


def combination(a, b):
    i = 1
    for _i in range(a - b + 1, a + 1):
        i *= _i
    return i // math.factorial(b)


def solve(string):
    n, m = map(int, string.split())
    primes = get_primes(m)
    m_copy = m
    divides = dict()
    for _p in primes:
        while m_copy % _p == 0:
            m_copy = m_copy // _p
            if str(_p) in divides.keys():
                divides[str(_p)] += 1
            else:
                divides[str(_p)] = 1
    if m_copy > 1:
        divides[str(m_copy)] = 1

    ans = 1
    for i in divides.values():
        ans *= combination(i + n - 1, i)
    return str(ans % (1000000007))


if __name__ == '__main__':
    print(solve(input()))
