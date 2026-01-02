def examA():
    N, i = LI()
    ans = N - i + 1
    print(ans)
    return

def examB():
    H, W = LI()
    A = [SI() for _ in range(H)]
    h = [[]for _ in range(H)]
    for i in range(W):
        flag = False
        for j in range(H):
            if A[j][i]=="#":
                flag = True
                break
        if flag:
            for j in range(H):
                h[j].append(A[j][i])
    #print(h)
    ans = []
    for i,a in enumerate(h):
        if "#" in a:
            ans.append(i)
    for v in ans:
        print("".join(map(str,h[v])))
    return

def examC():
    N, K = LI()
    X = LI()
    ans = inf
    for i in range(N-K+1):
        if X[i]<0 and X[i+K-1]>0:
            cur = (-X[i] + X[i+K-1]) + min(-X[i], X[i+K-1])
        else:
            cur = max(-X[i], X[i+K-1])
        ans = min(ans,cur)
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math,random
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

if __name__ == '__main__':
    examC()

"""

"""