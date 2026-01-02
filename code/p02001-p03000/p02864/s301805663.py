def examA():
    N = DI()/dec(7)
    ans = N
    print(N)
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
    ans = 0
    print(ans)
    return

def examF():
    N, K = LI()
    H = LI()
    H.insert(0,0)
    dp = [[[inf]*(K+1)for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        for j in range(i+1):
            for k in range(K+1):
                dp[i+1][i+1][k] = min(dp[i+1][i+1][k],dp[i][j][k]+max(0,H[i+1]-H[j]))
                if k<K:
                    dp[i+1][j][k+1] = min(dp[i+1][j][k+1],dp[i][j][k])

    ans = inf
    for j in range(N+1):
        ans = min(ans,dp[-1][j][-1])
    #for v in dp:
    #    print(v)
    print(ans)
    return

from decimal import getcontext,Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

getcontext().prec = 28

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examF()

"""
8 7
7 3 9 1 5 2 8 3
"""