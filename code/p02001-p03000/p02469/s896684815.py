# python template for atcoder1
from functools import reduce
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def gcd(a, b):
    """
    return gcd of a,b
    ユークリッド
    """
    while b:
        a, b = b, a % b
    return a


def list_gcd(l):
    """
    l: list
    l のgcd を返す
    """
    return reduce(gcd, l)


def lcm(a, b):
    """
    a,bの最小公倍数
    """
    return a*b//gcd(a, b)


def list_lcm(l):
    """
    l:list
    lのlcmを返す
    """
    return reduce(lcm, l)


n = int(input())
l = list(map(int, input().split()))
print(list_lcm(l))

