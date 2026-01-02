from itertools import groupby
from operator import mul
from functools import reduce

N, M = map(int, input().split())
mod = 10 ** 9 + 7


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    p = [len(list(j)) for i, j in groupby(prime_factorize(M))]
    answer = 1
    for i in p:
        answer *= cmb(i + N - 1, N - 1)
        answer %= mod

    print(answer)


if __name__ == '__main__':
    main()
