from bisect import bisect_right, bisect_left
from collections import Counter, deque
from functools import lru_cache, reduce
from heapq import heappop, heappush
from itertools import groupby, permutations, combinations, product
from sys import stdin, stderr


# 最大公約数（ユークリッドの互除法）
# Python3.5 で math.gcd()が追加され、
# AtCoder環境と最新環境でパッケージが分かれてしまったので、自分で書いておく
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


# 拡張ユークリッド互除法
# 正整数x, y について、a*x + b*y == gcd(x,y)なるa,bを返す。
# 特に、互いに素なるx, yについては a*x + b*y == 1 となる a, b。
def exgcd(x, y):
    if y == 0:
        return 1, 0
    a, b = exgcd(y, x % y)
    return b, a - (x // y) * b


# 最小公倍数
def lcm(x, y):
    m = gcd(x, y)
    return (x // m) * (y // m)


def mod_fac(n, r):
    mod = 10 ** 9 + 7
    res = 1
    for i in range(r):
        res = res * (n - i) % mod
    return res


def mod_pow(x, n):
    res = 1
    mod = 10**9 + 7
    while n > 0:
        if n % 2 == 1:
            res *= x
            res %= mod
        x *= x
        x %= mod
        n //= 2
    return res


def mod_comb(n, r):
    r = min(r, n-r)
    mod = 10 ** 9 + 7
    res = mod_fac(n, r)
    return res * mod_pow(mod_fac(r, r), mod - 2) % mod


def main():
    mod = 10**9 + 7
    n, a, b = [int(x) for x in input().split()]
    ret = mod_pow(2, n) - 1
    # print(ret, mod_comb(n,a), mod_comb(n, b))
    ret -= mod_comb(n, a)
    if ret < 0:
        ret += mod
    ret -= mod_comb(n, b)
    if ret < 0:
        ret += mod
    return ret


if __name__ == "__main__":
    print(main())