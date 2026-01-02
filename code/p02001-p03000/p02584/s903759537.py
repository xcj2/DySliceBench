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
    X, K, D = LI()
    X = abs(X)
    if X - K * D > 0:
        ans = X - K * D
    else:
        mi = X % D
        _mi = mi - D
        if abs(mi) > abs(_mi):
            mi = _mi # can be <0
        n_move = (X - mi) // D
        if n_move % 2 != K % 2:
            ans = min(abs(mi + D), abs(mi - D))
        else:
            a2 = abs(mi - D)
            ans = min(abs(mi), a2)
    print(ans)
main()

