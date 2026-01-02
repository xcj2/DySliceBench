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


N, X = LI()
X_list = LI()
X_list.sort()

bisect.insort_left(X_list, X)
#  print(X_list)
X_diff = [j-i for i, j in zip(X_list[:-1], X_list[1:])]
result = min(X_diff)
# 全部行けない場合がある
# 1 4 9 など
# すべてステップ幅-1で割り切れなければ不可

for i in range(result+1, 0, -1):
    if all(x % i == 0 for x in X_diff):
        print(i)
        exit()

