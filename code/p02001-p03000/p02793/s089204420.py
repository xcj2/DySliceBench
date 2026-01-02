# -*- coding: utf-8 -*-
from sys import stdin
# import numpy as np
# import sys
# sys.setrecursionlimit(10**4)

def _li(): return list(map(int, stdin.readline().split()))
def _li_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def _lf(): return list(map(float, stdin.readline().split()))
def _ls(): return stdin.readline().split()
def _i(): return int(stdin.readline())
def _f(): return float(stdin.readline())
def _s(): return stdin.readline()[:-1]
MOD = 10**9 + 7


def gcd(a, b):
    """ Greatest Common Divisor(最大公約数) """
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """ Least Common Multiple(最小公倍数) """
    return a * (b // gcd(a, b))


def calc_inverse_element_with_Fermat(a, MOD):
    """
    法をMODとしたときのaの逆元bを返す
    Fermatの小定理を用いる
    a * b = 1 (mod = MOD)

    Attention
    ---------
    MOD は素数の必要がある
    """
    return pow(a, MOD-2, MOD)


N = _i()
a_list = _li()

a_lcm = 1
for a in a_list:
    a_lcm = lcm(a_lcm, a)

a_lcm %= MOD
ans = 0
for a in a_list:
    ans = (ans + a_lcm * calc_inverse_element_with_Fermat(a, MOD)) % MOD
print(ans)
