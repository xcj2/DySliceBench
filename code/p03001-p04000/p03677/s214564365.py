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
    S = [0]*(M+2)
    for i in range(N-1):
        a0, a1 = A[i:i+2]
        S[a0+1] += 1
        S[a1] -= 1
        if a1<a0:
            S[0] += 1
    #print(S)
    for i in range(M):
        S[i+1] += S[i]
    for i in range(M+1):
        if S[i]<0:
            S[i] = 0
    D = defaultdict(int)
    for i in range(N-1):
        a0, a1 = A[i:i+2]
        cost = (a1 + M - a0) % M - 1
        D[a1] += cost
    start = 0
    for i in range(N-1):
        a0, a1 = A[i:i+2]
        cost = min(a1, (a1+M-a0)%M)
        start += cost
    #print(S)
    #print(D)
    #print(start)
    cost = start
    ans = start
    for i in range(1,M):
        cost += (D[i] - S[i])
        #print(cost)
        if ans>cost:
            ans = cost
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
def I(): return int(input())
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

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""