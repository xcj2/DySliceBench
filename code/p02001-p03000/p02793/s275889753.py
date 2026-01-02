from functools import reduce

MOD = 10**9+7


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


N = int(input())
L = list(map(int, input().split()))

LCM = list_lcm(L)
print(sum([LCM//v for v in L]) % MOD)
