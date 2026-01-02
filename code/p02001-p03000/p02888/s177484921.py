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
    L = LI()
    L = sorted(L)
    cnt = 0
    for i in range(N-1):
        a = L[i]
        for j in range(i+1, N-1):
            b = L[j]
            ok = j + 1
            ng = N - 1
            # ensure ok
            if L[ok] >= a + b:
                ok = ng = j
            # ensure ng is not ok
            elif L[ng] < a + b:
                ok = ng = N - 1
            else:
                pass

            while ng - ok > 1:
                m = (ok + ng) // 2
                c = L[m]
                if c < a + b:
                    ok = m
                else:
                    ng = m
            cnt += (ok - j)
    print(cnt)
main()

