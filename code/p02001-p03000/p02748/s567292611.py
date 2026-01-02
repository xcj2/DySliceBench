def examA():
    S = SI()
    if len(S)%2==1:
        print("No")
        return
    for i in range(len(S)//2):
        if S[i*2:i*2+2]!="hi":
            print("No")
            return
    print("Yes")
    return

def examB():
    a, b, M = LI()
    A = LI()
    B = LI()
    D = [LI()for _ in range(M)]
    ans = min(A) + min(B)
    for x,y,c in D:
        cur = A[x-1]+B[y-1]-c
        ans = min(ans,cur)
    print(ans)
    return

def examC():
    ans = 0
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
    examB()

"""

"""