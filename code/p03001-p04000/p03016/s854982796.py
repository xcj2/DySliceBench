#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS():return list(map(list, sys.stdin.readline().split()))
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = I()
    return l
def LIR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LI()
    return l
def SR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = S()
    return l
def LSR(n):
    l = [None for i in range(n)]
    for i in range(n):l[i] = LS()
    return l
sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    p,q,r = LI()
    print(p+q+r-max(p,q,r))
    return

#B
def B():
    n = I()
    w = LI()
    ans = float("inf")
    for i in range(n):
        m = sum(w[:i])
        l = sum(w[i:])
        ans = min(ans,abs(m-l))
    print(ans)
    return

#C
def C():
    n,m = LI()
    f = [1 for i in range(n+10000)]
    for i in range(m):
        a = I()
        f[a] = 0
    dp = [0 for i in range(n+10000)]
    dp[0] = 1
    for i in range(n):
        if f[i+1]:
            dp[i+1] += dp[i]
            dp[i+1] %= mod
        if f[i+2]:
            dp[i+2] += dp[i]
            dp[i+2] %= mod
    print(dp[n])
    return

#D
def D():
    h,w = LI()
    s = SR(h)
    vi = [[0 for j in range(w)] for i in range(h)]
    ho = [[0 for j in range(w)] for i in range(h)]
    q = deque()
    for y in range(h):
        for x in range(w):
            if s[y][x] == "#":
                l = len(q)
                while q:
                    i,j = q.pop()
                    vi[i][j] = l
            else:
                q.append((y,x))
        l = len(q)
        while q:
            i,j = q.pop()
            vi[i][j] = l
    for x in range(w):
        for y in range(h):
            if s[y][x] == "#":
                l = len(q)
                while q:
                    i,j = q.pop()
                    ho[i][j] = l
            else:
                q.append((y,x))
        l = len(q)
        while q:
            i,j = q.pop()
            ho[i][j] = l
    ans = 0
    for y in range(h):
        for x in range(w):
            ans = max(ans,vi[y][x]+ho[y][x]-1)
    print(ans)
    return

#E
def E():
    b = S()
    l = len(b)
    for i in range(l):
        b[i] = int(b[i])
    dp = [[0 for j in range(2)] for i in range(1000002)]
    dp[0][0] = 1
    for i in range(l):
        for j in range(2):
            x = 1 if j else b[i]
            for d in range(x+1):
                if d:
                    dp[i+1][j or d < b[i]] += 2*dp[i][j]
                    dp[i+1][j or d < b[i]] %= mod
                else:
                    dp[i+1][j or d < b[i]] += dp[i][j]
                    dp[i+1][j or d < b[i]] %= mod
    ans = 0
    for j in range(2):
        ans += dp[l][j]
        ans %= mod
    print(ans)
    return

#F
def F():
    def dot(a,b,m):
        return sum(list(map(lambda x:x[0]*x[1]%m, zip(a,b))))%m

    def mat_mul(a,b,m):
        b_ = [[b[i][j] for i in range(len(b))] for j in range(len(b[0]))]
        return [[dot(a[i],b_[j],m) for j in range(len(b_))] for i in range(len(a))]

    def mat_pow(a,n,m):
        res = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
        while n:
            if n&1:
                res = mat_mul(res,a,m)
            n >>= 1
            a = mat_mul(a,a,m)
        return res

    l,a,b,m = LI()
    ans = 0
    p = 1
    s = 0
    for d in range(1,19):
        left = max(0,-((a-p)//b))
        if left >= l:
            break
        p *= 10
        right = min(l,-((a-p)//b))
        if right <= left:
            continue
        mat = mat_pow([[p,1,0],[0,1,1],[0,0,1]],right-left,m)
        ans *= pow(10,d*(right-left),m)
        ans += (mat[0][1]*(a+b*left)%m+mat[0][2]*b%m)%m
        ans %= m
    print(ans)
    return

#Solve
if __name__ == "__main__":
    F()
