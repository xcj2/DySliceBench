def examA():
    S = SI()
    if S[2]==S[3] and S[4]==S[5]:
        print("Yes")
    else:
        print("No")
    return

def examB():
    X = I()
    ans = 0
    ans += (X//500) * 1000
    X %= 500
    ans += (X//5) * 5
    print(ans)
    return

def examC():
    K, N = LI()
    A = LI()
    L = [0]*N
    L[0] = K-A[-1] + A[0]
    for i in range(1,N):
        L[i] = A[i]-A[i-1]
    ans = sum(L) - max(L)
    #print(L)
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
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = 10**(-12)
alphabet = [chr(ord('a') + i) for i in range(26)]

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    examC()

"""

"""