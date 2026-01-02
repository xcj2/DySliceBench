"""
最大公約数を求める
最大公約数の約数を列挙
素数かどうかを判定
"""

import math

def divisor(n): #nの約数を全て求める
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return table

def max_yakusu(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(n):
    """素数判定関数

    Arguments:
        n {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True

A, B = map(int,input().split())

gcd = max_yakusu(B,A)
numbers = divisor(int(gcd))
ans = 0
for i in numbers:
    if is_prime(i):
        ans += 1
print(ans)