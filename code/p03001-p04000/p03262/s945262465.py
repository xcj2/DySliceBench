import numpy as np
import functools
import sys
sys.setrecursionlimit(10**9)

# 最大公約数
def gcd_impl(n,m):
    for _ in range(10):
        t = n - m
        q = m > t
        if q:
            n = m
        else:
            n = t
        if q:
            m = t
        else:
            m = m
        if m == 0:
            return n
    return gcd_impl(m, n%m)

def gcd(n,m):
    if n > m:
        return gcd_impl(n,m)
    else:
        return gcd_impl(m,n)


def gcd_list(nums):
    return functools.reduce(gcd, nums)

N, X = map(int, input().split())
x = np.array(list(map(int, input().split())))
x = abs(X - x)
print(gcd_list(x))