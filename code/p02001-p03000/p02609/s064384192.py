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
     
def powmod(x, n, k):
    if k == 0:
        return 1

    ans = 1
    while(n > 0):
        if(bin(n & 1) == bin(1)):
            ans = ans*x
            ans %= k
        x = x*x
        x %= k
        n = n >> 1
    return ans % k

def popcnt(n):
    return bin(n).count("1")

def main():
    N = I()
    X = S()
    cnt = 0
    for i in range(len(X)):
        if int(X[i]) & 1  == 1:
            cnt += 1
    a = cnt + 1
    b = cnt - 1

    pow2a = [0] * (N+2)
    pow2b = [0] * (N+2) # 2 ^ i mod b

    suma = 0
    sumb = 0
    dX = X[::-1]
    for i in range(N+1):
        pow2a[i] = powmod(2, i, a)
        pow2b[i] = powmod(2, i, b)
        if i >= len(dX):
            continue
        if b == 0:
            sumb = 0
            continue
        if int(dX[i]) == 1:
            suma += pow2a[i]
            sumb += pow2b[i]
            suma %= a
            sumb %= b
    # rev
    X = X[::-1]
    # i=0 -> 2^(len(X) - i)
    # 0 ... len(X) - 1
    subx = []
    ans = [1] * N
    for i in range(len(X)):
        cp_suma = suma
        cp_sumb = sumb
        if int(X[i]) == 0:
            # 1にするので、加算してからaでわる
            # i = 0なら2^0 = 1のくらい
            cp_suma += pow2a[i]
            cp_suma %= a
            res = cp_suma
        else:
            # 0 にするので引き算してからbでわる
            if b == 0:
                ans[N-1-i] -= 1
                subx.append(0)
                continue
            cp_sumb -= pow2b[i]
            cp_sumb %= b
            res = cp_sumb
        subx.append(res)

    subx = subx[::-1]
    for i, a in enumerate(subx):
        while a > 0:
            a %= popcnt(a)
            ans[i] += 1
    for a in ans:
        print(a)


main()

