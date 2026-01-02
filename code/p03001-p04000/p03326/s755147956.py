def examA():
    N = I()
    ans = ((N+1)//2)/N
    print(ans)
    return

def examB():
    N, K = LI()
    H = [I()for _ in range(N)]
    H.sort()
    ans = inf
    for i in range(N-K+1):
        cur = H[i+K-1]-H[i]
        if ans>cur:
            ans = cur
    print(ans)
    return

def examC():
    N = I()
    A = LI()
    ans = [0]*N
    C = Counter(A)
    base = 0
    for c in C.values():
        base += c*(c-1)//2
    #print(C)
    #print(base)
    for i in range(N):
        ans[i] = base - (C[A[i]]-1)
    for v in ans:
        print(v)
    return

def examD():
    N, K = LI()
    X = LI()
    L = []; R = [0]
    for x in X:
        if x<0:
            L.append(-x)
        else:
            R.append(x)
    L.append(0)
    L = L[::-1]
    ans = inf
    for i in range(len(L)):
        if len(R)<=K-i:
            continue
        cur = min(L[i] * 2 + R[K - i], L[i] + R[K - i] * 2)
        # print(cur)
        if ans > cur:
            ans = cur
    print(ans)
    return

def examE():
    N, M = LI()
    X = [LI()for _ in range(N)]
    ans = 0
    for i1 in [-1,1]:
        for i2 in [-1,1]:
            for i3 in [-1,1]:
                curX = [0]*N
                for i in range(N):
                    curX[i] = X[i][0]*i1+X[i][1]*i2+X[i][2]*i3
                curX.sort(reverse=True)
                cur = sum(curX[:M])
                if ans<cur:
                    ans = cur
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
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""