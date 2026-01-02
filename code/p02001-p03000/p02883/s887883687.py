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
    n, k = LI()
    a = sorted(LI())
    f = sorted(LI())[::-1]
    ok = 10**12
    ng = -1

    def can(x):
        times = 0
        for i in range(n):
            if f[i] * a[i] > m:
                times += ((f[i] * a[i] - m) // f[i] + 1)
                if (f[i] * a[i] - m) % f[i] == 0:
                    times -= 1
        if times <= k:
            return True
        return False

    while ok > ng + 1:
        m = (ok + ng) // 2
        if can(m):
            ok = m
        else:
            ng = m
    print(ok)

main()

