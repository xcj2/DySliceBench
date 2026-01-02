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


def main():
    n, r = [int(x) for x in input().split()]
    if n >= 10:
        return r
    return 100*(10-n) + r


if __name__ == "__main__":
    print(main())