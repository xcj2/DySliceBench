def examA():
    N = SI()
    ans = "No"
    for s in N:
        if s=="7":
            ans = "Yes"
    print(ans)
    return

def examB():
    N = I()
    ans = 0
    for i in range(1,N+1):
        if i%3==0:
            continue
        if i%5==0:
            continue
        ans += i
    print(ans)
    return

def examC():
    def gcd(x, y):
        if y == 0:
            return x
        while (y != 0):
            x, y = y, x % y
        return x
    K = I()
    ans = 0
    for i in range(1,K+1):
        for j in range(1,K+1):
            cur = gcd(i,j)
            for k in range(1,K+1):
                ans += gcd(cur,k)
    print(ans)
    return

def examD():
    N = I()
    S = SI()
    R = [0]*(N+1)
    G = [0]*(N+1)
    B = [0]*(N+1)
    for i in range(N):
        s = S[i]
        R[i+1] += R[i]
        G[i+1] += G[i]
        B[i+1] += B[i]
        if s=="R":
            R[i+1] += 1
        elif s=="G":
            G[i+1] += 1
        elif s=="B":
            B[i+1] += 1
    ans = 0
    for l in range(N):
        Ls = S[l]
        for r in range(l+3,N):
            Rs = S[r]
            if (Ls=="R" and Rs=="B") or (Ls=="B" and Rs=="R"):
                ans += G[r] - G[l]
                if (l+r)%2==0:
                    if S[(l+r)//2]=="G":
                        ans -= 1
            elif (Ls=="R" and Rs=="G") or (Ls=="G" and Rs=="R"):
                ans += B[r] - B[l]
                if (l+r)%2==0:
                    if S[(l+r)//2]=="B":
                        ans -= 1
            elif (Ls=="G" and Rs=="B") or (Ls=="B" and Rs=="G"):
                ans += R[r] - R[l]
                if (l+r)%2==0:
                    if S[(l+r)//2]=="R":
                        ans -= 1
    print(ans)
    return

def examE():
    N, K = LI()

    ans = 0
    print(ans)
    return

def examF():
    N = I()
    A = LI()

    if N%2==0:
        O = [0] * N
        E = [0] * N
        for i in range(N):
            O[i] += O[i - 1]
            E[i] += E[i - 1]
            if i % 2 == 0:
                O[i] += A[i]
            else:
                E[i] += A[i]
        #print(O,E)
        ans = max(O[-1],E[-1])
        print(ans)
        return

    def dfs(n,k):
        if (n+2)//2 <k:
            return -inf
        if k == 0:
            return 0
        if n==0:
            if k==1:
                return A[0]
            return -inf
        if n==1:
            if k==1:
                return max(A[0],A[1])
            return -inf
        res = max(A[n]+dfs(n-2,k-1),dfs(n-1,k))
        return res

    ans = dfs(N-1,N//2)
    #print(dfs(4,2))
    print(ans)
    return

def examF2():
    N = I()
    A = LI()

    dp = [[-inf]*3 for _ in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0
    dp[1][0] = -inf
    dp[1][1] = 0
    dp[1][2] = A[0]
    for i in range(1,N):
        dp[i+1][2] = A[i] + dp[i-1][2]
        dp[i+1][1] = max(A[i] + dp[i-1][1],dp[i][2])
        dp[i+1][0] = max(A[i] + dp[i-1][0],dp[i][1])
    if N%2==1:
        ans = max(dp[-1][0],dp[-1][1])
    else:
        ans = max(dp[-1][1],dp[-1][2])
    #print(dp)
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
    examF2()

"""
27
18 18 19 28 -45 90 -45 23 -53 60 28 -74 -71 35 -26 -62 49 -77 57 24 -70 -93 69 -99 59 57 -49
"""