def examA():
    N = I()
    X = [LI()for _ in range(N)]
    l = 0; r = inf
    for _ in range(100):
        now = (l+r)/2
        x_l = -inf; x_r = inf
        y_l = -inf; y_r = inf
        for x,y,c in X:
            move = now / c
            x_l = max(x_l,x-move)
            x_r = min(x_r,x+move)
            y_l = max(y_l,y-move)
            y_r = min(y_r,y+move)
        if x_l<x_r and y_l<y_r:
            r = now
        else:
            l = now
    ans = r
    print(ans)
    return

def examB():
    N = I()
    C = LI()
    C.sort()
    base = pow(2,2*N-1,mod)
    inv = pow(2,mod-2,mod)
    ans = 0
    for i in range(N):
        cur = C[i]*base*(1+(N-1-i)*inv)
        ans += cur
        ans %= mod
    print(ans)
    return

def examC():
    N = I()
    Ag,As,Ab = LI()
    Bg,Bs,Bb = LI()
    dp = [i for i in range(N+1)]
    for i in range(N):
        if dp[i+1]<dp[i]:
            dp[i+1] = dp[i]
        if i+Ag<=N and dp[i+Ag]<dp[i]+Bg:
            dp[i+Ag] = dp[i]+Bg
        if i+As<=N and dp[i+As]<dp[i]+Bs:
            dp[i+As] = dp[i]+Bs
        if i+Ab<=N and dp[i+Ab]<dp[i]+Bb:
            dp[i+Ab] = dp[i]+Bb
    ne_N = dp[-1]
    #print(dp)
    dp2 = [i for i in range(ne_N+1)]
    for i in range(ne_N):
        if dp2[i+1]<dp2[i]:
            dp2[i+1] = dp2[i]
        if i+Bg<=ne_N and dp2[i+Bg]<dp2[i]+Ag:
            dp2[i+Bg] = dp2[i]+Ag
        if i+Bs<=ne_N and dp2[i+Bs]<dp2[i]+As:
            dp2[i+Bs] = dp2[i]+As
        if i+Bb<=ne_N and dp2[i+Bb]<dp2[i]+Ab:
            dp2[i+Bb] = dp2[i]+Ab
    ans = dp2[-1]
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
_ep = 10**(-7)
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