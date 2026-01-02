def examA():
    N, M = LI()
    if N==M:
        print("Yes")
    else:
        print("No")
    return

def examB():
    A, B = LI()
    if A>B:
        ans = str(B)*A
    else:
        ans = str(A)*B
    print(ans)
    return

def examC():
    N = I()
    P = LI()
    minP = N+1
    ans = 0
    for i in range(N):
        if minP>P[i]:
            minP=P[i]
            ans +=1
    print(ans)
    return

def examD():
    N = I()
    ans = 0
    keep = [[0]*10 for _ in range(10)]
    for i in range(1,N+1):
        l = int(str(i)[0]); r = int(str(i)[-1])
        keep[l][r]+=1

    for i in range(1,N+1):
        l = int(str(i)[0])
        r = int(str(i)[-1])
        ans += keep[r][l]

    print(ans)
    return

def examE():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x
    def lcm(x, y):
        return x * y // gcd(x, y)
    N = I()
    A = LI()


    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examD()

"""

"""