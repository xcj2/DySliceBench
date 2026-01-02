def examA():
    N = I()
    H = LI()
    dp = [inf]*(N)
    dp[0] = 0
    for i in range(N-1):
        dp[i+1] = min(dp[i+1],dp[i]+abs(H[i+1]-H[i]))
        if i<N-2:
            dp[i + 2] = min(dp[i + 2], dp[i]+abs(H[i + 2] - H[i]))
    ans = dp[-1]
    print(ans)
    return

def examB():
    N, K = LI()
    H = LI()
    dp = [inf]*N
    dp[0] = 0
    for i in range(N):
        for k in range(1,K+1):
            if i+k>=N:
                break
            if dp[i+k]>dp[i]+abs(H[i+k]-H[i]):
                dp[i+k] = dp[i]+abs(H[i+k]-H[i])
    ans = dp[-1]
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
    ans = 0
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
alphabet = [chr(ord('a') + i) for i in range(26)]

if __name__ == '__main__':
    examB()

"""

"""