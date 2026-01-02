import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = I()
    A = sorted(LI())
    n = A[-1]
    ix = bisect.bisect_left(A, n / 2)
    '''
    [1, 3, 8, 10, 12] -> bisect_left(A, 12 / 2) = 2
    [1, 2, 3, 8, 10, 12] -> bisect_left(A, 12/2) = 3
    '''
    m, l, r = inf, inf, inf
    # 最大値の半分との距離が最小のものを選ぶ
    if ix < N:
        m = A[ix]
    if 0 < ix <= N:
        l = A[ix - 1]

    m1 = abs(n / 2 - m)
    l1 = abs(n / 2 - l)

    min_val = min(m1, l1)
    if min_val == m1:
        n_ = m
    if min_val == l1:
        n_ = l

    print(n, n_)
main()

