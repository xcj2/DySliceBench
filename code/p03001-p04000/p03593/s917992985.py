def examA():
    N, M, A, B = LI()
    C = [I()for _ in range(M)]
    ans = 0
    for i,c in enumerate(C):
        if N<=A:
            N += B
        N -= c
        if N<0:
            ans = i+1
            break
    if ans==0:
        ans = "complete"
    print(ans)
    return

def examB():
    N = LI()
    P = LI()
    return

def examC():
    S = LSI()
    N = I()
    NG = [SI()for _ in range(N)]
    ans = []
    #print(S)
    for s in S:
        flag = True
        for ng in NG:
            if not flag:
                break
            if len(s)!=len(ng):
                continue
            f = True
            for i,t in enumerate(ng):
                if s[i]!=t and t!="*":
                    f = False
                    break
            if f:
                flag = False
                break
        if not flag:
            ans.append("*"*len(s))
        else:
            ans.append(s)
    print(" ".join(map(str,ans)))
    return

def examD():
    H, W = LI()
    S = [SI()for _ in range(H)]
    D = defaultdict(int)
    for s in S:
        for d in s:
            D[d] += 1
    odd = 1
    two = (H//2)*(W%2) + (W//2)*(H%2)
    for d in D.values():
        if d%2==1:
            odd -= 1
        elif d%4==2:
            two -= 1
    if odd<0 or two<0:
        print("No")
        return
    print("Yes")
    return

def examE():
    ans = 0
    print(ans)
    return

def examF():
    N, K = LI()
    S = SI()
    D = [defaultdict(int) for _ in range(N+1)]
    for i in range(N):
        D[i+1] = deepcopy(D[i])
        D[i+1][S[i]] += 1
    ans = "No"
    L = [defaultdict(int) for _ in range(N-K+1)]
    for i in range(N-K+1):
        cur = deepcopy(D[i+K])
        for s,j in D[i].items():
            cur[s] -= j
        L[i] = cur



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
    examD()

"""
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""