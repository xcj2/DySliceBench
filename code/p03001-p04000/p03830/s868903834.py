#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def yakusu(n):
    ans = []
    for i in range(1, int(n**(1/2)//1) + 1):
        if n % i == 0:
            ans.append(i)
            ans.append(int(n / i))
    return list(set(ans))


def factorize(n):
    factorial_list = []

    b = 2
    while b * b <= n:
        while n % b == 0:
            n //= b
            factorial_list.append(b)
        b += 1

    if n > 1:
        factorial_list.append(n)
    return factorial_list


MOD = 10 ** 9 + 7


def main():
    N = II()

    fractals = [0] * (N + 1)

    for i in range(1, N+1):
        tmp = factorize(i)
        for fact in tmp:
            fractals[fact] += 1

    ans = 1
    for i in fractals:
        ans *= i + 1
        ans %= MOD

    print(ans)


main()
