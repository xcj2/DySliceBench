import math, string, itertools, fractions, heapq, collections, re,  array, bisect, sys, random, time, copy, functools
import numpy as np

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
    N = I()
    A = LI()
    #  print(N, A)


    # 余りを活用する
    A = list(set(A))
    A.sort(reverse=True)
    if A[-1] == 0:
        del A[-1]
    #  print(A)
    while len(A) > 1:
        #  A[0] = A[0] % A[1]
        A = [a % A[idx+1] if idx < len(A) - 1 else a for idx, a in enumerate(A)]
        A = list(set(A))
        A.sort(reverse=True)
        if A[-1] == 0:
            del A[-1]

        #  if A[0] == 0:
        #      del A[0]

    print(A[0])

main()
