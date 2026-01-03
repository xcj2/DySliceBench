def examA():
    S = SI()
    T = SI()
    N = len(S)
    ans = "No"
    for i in range(N):
        cur = S[i:] + S[:i]
        #print(cur)
        if cur==T:
            ans = "Yes"
    print(ans)
    return

def examB():
    H, W = LI()
    S = [SI()for _ in range(H)]
    flag = True
    ans = 0
    print(ans)
    return

def examC():
    L, R = LI()
    ans = inf
    if R-L>=3000:
        R = L+3000

    for l in range(L, R + 1):
        for r in range(l+1, R + 1):
            now = (l*r) %2019
            ans = min(ans,now)
    print(ans)
    return

def examD():
    T = {"dream", "dreamer", "erase", "eraser"}
    S = SI()
    ans = "NO"
    t = ""
    for s in S[::-1]:
        t += s
        if t[::-1] in T:
            t = ""
        if len(t)>10:
            print(ans)
            return
    if t=="":
        ans = "YES"
    print(ans)
    return

def examE():
    N = 50
    K = I()
    base = K//N
    A = [base+i for i in range(N)]
    rest = K%N
    for i in range(rest):
        A[-i-1] += 1
    print(N)
    print(" ".join(map(str,A)))
    return

def examF():
    N = 20
    C = [2**i for i in range(N)]
    L = I()
    cur = 1
    V = [[i+1, i+2, 0]for i in range(N-1)]
    now = 1
    while(now<N):
        if C[now]<=L:
            cur = C[now]
            V.append([now,now+1,C[now-1]])
            now += 1
        else:
            break
    #print(cur)

    for i in range(now)[::-1]:
        if C[i]<=L-cur:
            cost = cur
            V.append([i+1,N,cost])
            cur += C[i]

    print(N,len(V))
    for s,t,c in V:
        print(s,t,c)
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
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""