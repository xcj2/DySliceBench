import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
    
fac = [-1] * (10**7+1)
inv = [-1] * (10**7+1)
finv = [-1] * (10**7+1)

fac[0] = fac[1] = 1
inv[1] = 1
finv[0] = finv[1] = 1

def initNCMMod(limit):
    for i in range(2, limit):
        fac[i] = fac[i-1] * i

def NCM(n):
    return n * (n-1) // 2
def main():
    N = I()
    A = LI()
    vals = [0 for _ in range(N+1)]
    pick = [0 for _ in range(N+1)]
    for a in A:
        vals[a] += 1
    for i, val in enumerate(vals):
        pick[i] = NCM(val)
    picksum = sum(pick)
    for a in A:
        tmp_picksum = picksum - NCM(vals[a])
        tmp_picksum += NCM(vals[a]-1)
        print(tmp_picksum)


main()

