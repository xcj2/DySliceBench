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
    a = LI()
    b = LI()
    cnt = 0
    for i in range(len(b)):
        left = min(a[i], b[i])
        cnt += left
        b[i] -= left

        right = min(a[i+1], b[i])
        cnt += right
        b[i] -= right
        a[i+1] -= right
    print(cnt)
    """
    a = [0] + a
    b = [0] + b + [0]
    cnt = 0
    for i in range(1, N+2):
        if a[i] - b[i-1] >= 0:
            cnt += b[i-1]
            a[i] = a[i] - b[i-1]
            b[i-1] = 0
        else:
            cnt += a[i]
            b[i-1] = b[i-1] - a[i]
            a[i] = 0

        if a[i] - b[i] >= 0:
            cnt += b[i]
            a[i] = a[i] - b[i]
            b[i] = 0

        else:
            cnt += a[i]
            b[i] = b[i] - a[i]
            a[i] = 0
    print(cnt)
    """

main()

