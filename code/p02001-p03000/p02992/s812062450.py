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
    n = int(N**0.5)
    C = [] # N//j=indexとなるjの個数
    L = [0]*(2*int(n)) # N//indexの解 =>要りません。。
    for i in range(1,n+1):
        now = N//i - N//(i+1)
        C.append(now)
    for i in range(1,n+1):
        if N//i==i:
            continue
        C.append(1)
    C.reverse()
    #print(C)
    n = len(C)
    #for i in range(1,n+1):
    #    L[i-1] = N//i
    #for i in range(n):
    #    L[i+n] = n - i
    #L.reverse()
    #print(L)
    dp = [[0]*(n) for _ in range(K)]

    for i in range(n):
        dp[0][i] = C[i]
    #print(dp[0])
    for i in range(K-1):
        S = 0
        for j in range(n):
            S += dp[i][j]
            S %= mod
            dp[i+1][n-j-1] = S*C[n-j-1] %mod
    #print(dp)
    ans = 0
    for s in dp[-1]:
        ans += s
        ans %= mod
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
142
12 9 1445 0 1
asd dfg hj o o
aidn
"""