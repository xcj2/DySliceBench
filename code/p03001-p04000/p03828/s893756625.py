#! /usr/bin/python3
# Factors of Factorial

"""
1≦N≦103
"""

import math
import collections
# import sympy

test = False

N = int(input())


def prime_factors(n):
    """
    自然数 n の素因数のリスト
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            # n = n // i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def yakusu_no_kosu(n):
    """
    n! の約数の個数
    """

    l = prime_factors(math.factorial(n))
    c = collections.Counter(l)
    l_c = list(c.values())
    if test:
        print('l =', l)
        print('c =', c)
        print('l_c =', l_c)


    kosu = 1
    # 約数の数
    for v in l_c:
        kosu *= v + 1
    # 各素因数(key)の個数v(value)から約数の個数を算出

    """
    d = sympy.factorint(math.factorial(n))
    # n!を素因数分解 {素因数1: 個数, 素因数2: 個数, …}
    l_d = list(d.values())
    # 各素因数(key)の個数(value)のみリストにする

    if test:
        print('l_d =', l_d)

    kosu = 1
    # 約数の数

    for v in l_d:
        kosu *= v + 1
    # 各素因数(key)の個数v(value)から約数の個数を算出
    """

    return kosu


def main():
    """
    N! の約数の個数を 10^9+7 で割った余りを出力
    """
    print(yakusu_no_kosu(N) % (10**9 + 7))


if __name__ == '__main__':
    main()
