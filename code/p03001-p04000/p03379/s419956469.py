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
    X = LI()
    ans = [0] * N
    sorted_X = sorted([(x, i) for i, x in enumerate(X)], key=lambda x: x[0])
    l = sorted_X[N//2 - 1][0]
    r = sorted_X[N//2][0]
    for i, (x, org_ix) in enumerate(sorted_X):
        if i < N//2:
            _ans = r
        else:
            _ans = l
        ans[org_ix] = _ans
    for a in ans:
        print(a)
main()

