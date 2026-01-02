def examA():
    N = I()
    ans = 0
    print(ans)
    return

def examB():
    ans = 0
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
    N, M = LI()
    A = LI()
    A.sort()
    ma = max(A)
    l = 0; r = ma*2+1
    while(r-l>1):
        now = (l+r)//2
        cnt = 0
        for a in A:
            need = now-a
            if need>ma:
                continue
            c = bisect.bisect_left(A,need)
            cnt += N-c
        if cnt>=M:
            l = now
        else:
            r = now
    base = l
    cnt = 0
    ans = 0
    S = [0]+A
    for i in range(N):
        S[i+1] += S[i]
    #print(S)
    for a in A:
        need = base - a
        c = bisect.bisect_left(A, need+1)
        ans += a*(N-c) + S[N]-S[c]
        cnt += (N-c)
    if cnt<M:
        ans += base*(M-cnt)
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
    examE()

"""

"""