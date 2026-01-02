def examA():
    R = I()
    ans = R*2*3.141592
    print(ans)
    return

def examB():
    N, M = LI()
    A = LI()
    S = sum(A)
    if N>=S:
        ans = N-S
    else:
        ans = -1
    print(ans)
    return

def examC():
    N = I()
    A = LI()
    ans = [0]*N
    for i in range(N-2,-1,-1):
        ans[A[i]-1] +=1
    for v in ans:
        print(v)
    return

def examD():
    N, K = LI()
    S = [0]*(N+2)
    for i in range(1,N+1):
        S[i+1] = S[i] + i
    #print(S)
    ans = 0
    for i in range(K,N+2):
        cur = (S[N+1] - S[N-i+1]) - (S[i] - S[0]) +1
        ans += cur
        ans %= mod
        #print(cur)

    print(ans)
    return

def examE():
    N = I()
    A = LI()
    S = [[]for _ in range(N)]
    for i in range(N):
        S[i] = [A[i],i]
    S.sort(reverse=True)
    #print(S)
    dp = [[0]*(N+1)for _ in range(N+1)]
    for i in range(N):
        s, x = S[i]
        for j in range(i+1):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + s*(x-j))
            dp[i+1][j] = max(dp[i+1][j],dp[i][j] + s*(N-i-x+j-1))
            #print(N-i-x+j-1)
    ans = max(dp[-1])
    print(ans)
    #print(dp)
    return

def examF():
    N = I()
    C = LI()
    V = [[]for _ in range(N)]
    for _ in range(N-1):
        a, b = LI()
        a -= 1; b -= 1
        V[a].append(b)
        V[b].append(a)
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