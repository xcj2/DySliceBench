from sys import stdin
import numpy as np
mod = 10**9+7
X, Y = [int(x) for x in stdin.readline().rstrip().split()]


def mul(a, b):
    return ((a % mod) * (b % mod)) % mod


def div(a, b):
    return mul(a, pow(b, mod-2, mod))


def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        f %= mod
    return f


A = np.matrix([[2, 1], [1, 2]])
Y = np.matrix([[X], [Y]])
if np.linalg.matrix_rank(np.c_[A, Y]) == np.linalg.matrix_rank(A):
    x, y = np.linalg.solve(A, Y)
    x = float(x)
    y = float(y)
    if x < 0 or y < 0:
        print(0)
    elif (not x.is_integer()) or (not y.is_integer()):
        print(0)
    else:
        x = int(x)
        y = int(y)
        ans = fact(x+y)
        ans = div(ans, fact(x))
        ans = div(ans, fact(y))
        print(ans % mod)
else:
    print(0)