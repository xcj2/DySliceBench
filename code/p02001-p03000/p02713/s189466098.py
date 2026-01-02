def examA():
    N = SI()
    ans = "No"
    for s in N:
        if s=="7":
            ans = "Yes"
    print(ans)
    return

def examB():
    N = I()
    ans = 0
    for i in range(1,N+1):
        if i%3==0:
            continue
        if i%5==0:
            continue
        ans += i
    print(ans)
    return

def examC():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x
    K = I()
    ans = 0
    for i in range(1,K+1):
        for j in range(1,K+1):
            cur = gcd(i,j)
            for k in range(1,K+1):
                ans += gcd(cur,k)
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(readline())
def LI(): return list(map(int,readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examC()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""