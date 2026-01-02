def examA():
    N, M = LI()
    l = 1; r = N
    for _ in range(M):
        L, R = LI()
        l = max(L,l)
        r = min(R,r)
    ans = max(0,r-l+1)
    print(ans)
    return

def examB():
    N = I()
    S = [I()for _ in range(N)]
    rest = []
    for s in S:
        if s%10==0:
            continue
        rest.append(s)
    if sum(S)%10==0:
        if not rest:
            print(0)
            return
        ans = sum(S) - min(rest)
    else:
        ans = sum(S)
    print(ans)
    return

def examC():
    N, K = LI()
    K -= 1
    A = LI()
    L = A.index(1)
    #print(L)
    ans = (N-1+K-1)//K
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
def SI(): return read().rstrip().decode('utf-8')
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