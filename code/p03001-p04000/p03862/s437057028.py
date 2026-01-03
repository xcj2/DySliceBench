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
    N, x = LI()
    A = LI()
    cnt = 0
    for i in range(N-1):
        l = A[i]
        r = A[i+1]
        extra = l + r - x
        if extra <= 0:
            continue
        if extra <= r:
            A[i+1] = r - extra
        else:
            r = 0
            l = l - (extra - r)
            A[i+1] = r
            A[i] = l
        cnt += extra
    print(cnt)
main()

