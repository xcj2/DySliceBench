#  import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
import sys
import numpy as np


#  sys.setrecursionlimit(10**7)
#  inf = 10 ** 20
#  eps = 1.0 / 10**10
#  mod = 10**9+7
#  dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
#  ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)

def main():
    N = I()
    h = LI()
    h = np.array(h)
    #  print(N, h)
    # 0以上の塊をみつける
    # その塊に水をやる
    # 以上を繰り返す
    count = 0
    while True:
        #  print(h)
        first_non_zero_idx = [idx for idx, i in enumerate(h) if i != 0]
        if len(first_non_zero_idx) == 0:
            # 終了
            print(count)
            return
        else:
            first_non_zero_idx = first_non_zero_idx[0]

        first_zero_idx = [idx for idx, i in enumerate(h) if idx > first_non_zero_idx and i == 0]
        if len(first_zero_idx) == 0:
            # 0がないので最後まで水をやる
            first_zero_idx = len(h)
        else:
            first_zero_idx = first_zero_idx[0]

        # 水をやる
        min_value = min(h[first_non_zero_idx:first_zero_idx])
        h[first_non_zero_idx:first_zero_idx] -= min_value
        count += min_value





main()
