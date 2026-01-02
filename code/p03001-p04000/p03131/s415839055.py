import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools


sys.setrecursionlimit(10**7)
inf = 10 ** 20
eps = 1.0 / 10**10
mod = 10**9+7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    K, A, B = LI()
    result = 0
    # 交換する価値もない
    if A >= B - 1:
        # 割りまくる
        result = K + 1
        print(result)
        return

    # 交換をできるだけする
    # 最初に円にできるまでにどれだけかかるか？？
    times_to_first_yen = A - 1
    # K - times_to_first_yenはひたすら交換しまくる
    remaining_times = K - times_to_first_yen
    result += (remaining_times // 2) * (B - A) + A
    # 端数の処理をする
    if remaining_times % 2 != 0:
        result += 1

    print(result)


main()
