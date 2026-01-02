from functools import lru_cache
import sys


def count(n):
    c = 0
    for s in str(n):
        if s != "0":
            c += 1
    return c


@lru_cache()
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def C(i, j):
    return fact(i) // (fact(j) * fact(i - j))


def calc(N, K):
    if K==0:
        return 1
    if N < 10000:
        retval = 0
        for i in range(N + 1):
            if count(i) == K:
                retval += 1
        return retval

    keta = len(str(N))
    retval = C(keta - 1, K) * (9**K)
    retval += calc(int(str(N)[1:]),K-1)
    retval += (int(str(N)[0])-1)*calc(10**(keta-1)-1,K-1)
    return retval



N = int(input())
K = int(input())

print(calc(N,K))
