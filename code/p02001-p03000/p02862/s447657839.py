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

fac = [-1] * (10**7+1)
finv = [-1] * (10**7+1)
inv = [-1] * (10**7+1)

fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

def initNCMMod(limit):
    for i in range(2, limit):
        fac[i] = fac[i-1] * i % mod
        inv[i] = mod - inv[mod%i] * (mod // i) % mod
        finv[i] = finv[i-1] * inv[i] % mod

initNCMMod(666670)

def NCMMod(n, k):
    if n < k:
        return 0
    if (n < 0 or k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

def main():
    X, Y = LI()
    if (2 * X - Y) % 3 > 0:
        ans = 0
    elif (2 * Y - X) % 3 > 0:
        ans = 0
    else:
        i = (2 * X - Y) // 3
        j = (2 * Y - X) // 3
        ans = NCMMod(i+j, i)
    print(ans)
    return

'''
def main():
    X, Y = LI()
    g = [[0 for _ in range(X+1)] for __ in range(Y+1)]
    def reachable(row, col):
        if row > Y or col > X:
            return 0
        if row == Y and col == X:
            return 1
        ans = reachable(row + 1, col + 2) % mod + reachable(row + 2, col + 1) % mod
        ans = ans % mod
        return ans
    print(reachable(0, 0))
'''
main()

