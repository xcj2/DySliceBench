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
    a = []
    a.append([int(x) for x in input().split()])
    a.append([int(x) for x in input().split()])
    a.append([int(x) for x in input().split()])
    N = int(input())
    for i in range(N):
        b = int(input())
        for j in range(3):
            for k in range(3):
                if a[j][k] == b:
                    a[j][k] = -1
    tate = [0, 0, 0]
    yoko = [0, 0, 0]
    naname = [0, 0]
    for i in range(3):
        for j in range(3):
            tate[i] += a[i][j]
            yoko[j] += a[i][j]
        naname[0] += a[i][i]
        naname[1] += a[i][2 - i]
    # print(tate)
    # print(yoko)
    # print(naname)
    if -3 in tate or -3 in yoko or -3 in naname:
        return "Yes"
    return "No"


if __name__ == "__main__":
    print(main())
