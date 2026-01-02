def examA():
    S = SI()
    if S=="ARC":
        ans = "ABC"
    else:
        ans = "ARC"
    print(ans)
    return

def examB():
    N, K = LI()
    snuke = set(range(1,N+1))
    for _ in range(K):
        d = I()
        A = LI()
        for a in A:
            snuke.discard(a)
    ans = len(snuke)
    print(ans)
    return

def examC():
    N, M = LI()
    H = LI()
    good = set(range(1,N+1))
    for _ in range(M):
        a, b = LI()
        if H[a-1]>=H[b-1]:
            good.discard(b)
        if H[b-1]>=H[a-1]:
            good.discard(a)
    ans = len(good)
    print(ans)
    return

def examD():
    X = I()
    #print(1000**5-999**5)
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            if a**5-b**5==X:
                print(a,b)
                return
    return

def examE():
    N = I()
    A = LI()
    B = [0]*N
    D = defaultdict(int)
    for i in range(N):
        B[i] = A[i]-i
        c = A[i]+i
        D[c] += 1
    #print(B)
    #print(D)
    ans = 0
    for b in B:
        ans += D[-b]
    print(ans)
    return

def examF():
    N, A, B, C = LI()
    S = [SI()for _ in range(N)]
    ans = [""]*N


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
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""