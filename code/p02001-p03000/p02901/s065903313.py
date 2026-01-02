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
    A = [[]for _ in range(M)]
    C = [0]*M
    for i in range(M):
        A[i], b = LI()
        c = LI()
        for j in range(b):
            C[i] += 2**(c[j]-1)
    loop = 2**N
    dp = [[inf]*loop for _ in range(M+1)]
    dp[0][0] = 0
    for i in range(M):
        for l in range(loop):
            dp[i + 1][l] = min(dp[i + 1][l],dp[i][l])
            next = l|C[i]
            if next==l:
                continue
            dp[i+1][next] = min(dp[i+1][next],dp[i][l] + A[i])
    ans = dp[M][loop-1]
    if ans==inf:
        print(-1)
    else:
        print(ans)
    return

def examF():
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
    examE()

"""

"""