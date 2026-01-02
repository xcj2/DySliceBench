from functools import reduce
import numpy as np


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd(*n):
    return reduce(_gcd, n)


def my_bisect(x):

    def find_pos(left, right):
        return left + (right - left - 1) // 2

    def func(left, right, prev):
        if right - left == 1:
            return left
        pos = find_pos(left, right)
        g1 = gcd(*x[left:pos+1])
        g2 = gcd(*x[pos+1:right])
        if prev is not None:
            g1, g2 = gcd(g1, prev), gcd(g2, prev)
        if g1 < g2:
            return func(left, pos + 1, max(g1, g2))
        else:
            return func(pos + 1, right, max(g1, g2))
    return func(0, len(x), None)


N = int(input())
A = list(map(int, input().split()))
print(gcd(*np.delete(A, my_bisect(A))))

