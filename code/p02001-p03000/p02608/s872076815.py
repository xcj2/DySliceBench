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
    nmax = 10**2
    ans = [0] * (10**4+1)
    for i in range(1, nmax):
        for j in range(1, nmax):
            for k in range(1, nmax):
                c = i*i + j*j + k*k + i*j + j*k + k*i
                if c > 10**4:
                    continue
                ans[c] += 1
    for i in range(1, N+1):
        print(ans[i])



main()

