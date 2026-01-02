def examA():
    AB = [I() for _ in range(2)]
    for i in range(1,4):
        if not i in AB:
            ans = i
            break
    print(ans)
    return

def examB():
    N = I()
    S,T = LSI()
    ans = ""
    for i in range(N):
        ans += S[i]+T[i]
    print(ans)
    return

def gcd(x, y):
    if y == 0:
        return x
    while y != 0:
        x, y = y, x % y
    return x
def lcm(x, y):
    return x * y // gcd(x, y)
def examC():
    A, B = LI()
    ans = lcm(A,B)
    print(ans)
    return

def examD():
    N = I()
    A = LI()
    ans = N; cur = 1
    for a in A:
        if cur==a:
            ans -=1
            cur +=1
    if ans==N:
        ans = -1
    print(ans)
    return

def examE():
    N = I()
    ans = 0
    if N%2==0:
        N //=2
        while(N>0):
            ans +=N//5
            N //=5
    print(ans)
    return

def examF():
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examE()
