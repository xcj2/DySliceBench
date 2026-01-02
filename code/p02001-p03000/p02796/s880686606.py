def examA():
    H = I()
    W = I()
    N = I()
    ans = (N-1)//max(H,W) + 1
    print(ans)
    return

def examB():
    N = I()
    XL = [LI()for _ in range(N)]
    for i in range(N):
        XL[i][0] += XL[i][1]
    XL.sort()
#    print(XL)
    ans = 0
    now = -inf
    for i in range(N):
        if XL[i][0]-XL[i][1]*2>=now:
            ans +=1
            now = XL[i][0]
    print(ans)
    return

def examC():
    return

def examD():
    return

def examE():
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
    examB()
