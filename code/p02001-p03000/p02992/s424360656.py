#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    s = S()
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    for i in d.keys():
        if d[i] != 2:
            print("No")
            quit()
    print("Yes")
    return

#B
def B():
    n = I()
    p = LI()
    ans = 0
    for i in range(1,n-1):
        k = p[i-1:i+2]
        k.sort()
        if k[1] == p[i]:
            ans += 1
    print(ans)
    return

#C
def C():
    n = I()
    d = LI()
    d.sort()
    print(d[n//2]-d[n//2-1])
    return

#D
def D():
    n,k = LI()
    fact = [1]*100001
    for i in range(1,100001):
        fact[i] = fact[i-1]*i%mod
    inv = [1]*100001
    inv[-1] = pow(fact[-1],mod-2,mod)
    for i in range(1,100001)[::-1]:
        inv[i-1] = inv[i]*i%mod

    for i in range(1,k+1):
        if n-k+1 < i:
            print(0)
        else:
            ans = fact[n-k+1]*inv[i]*inv[n-k+1-i]%mod
            ans *= fact[k-1]*inv[k-i]*inv[i-1]%mod
            ans %= mod
            print(ans)
    return

#E
def E():
    ma = 100000000
    def dijkstra(s):
        d = defaultdict(lambda : ma)
        q = [(0,s,0)]
        d[(s,0)] = 0
        while q:
            dx,x,t = heappop(q)
            t = (t+1)%3
            k = t == 1
            for y in v[x]:
                if dx+k < d[(y,t)]:
                    d[(y,t)] = dx+k
                    heappush(q,(d[(y,t)],y,t))
        res = d[(g,0)]
        if res == ma:
            res = -1
        return res

    n,m = LI()
    v = [[] for i in range(n)]
    for i in range(m):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
    s,g = LI()
    s -= 1
    g -= 1
    print(dijkstra(s))
    return

#F
def F():
    n,k = LI()
    if n == 1:
        print(1)
        quit()
    f = [0,n]
    i = 1
    while f[i] >= i:
        i += 1
        f.append(n//i)
    s = [0]*len(f)
    for i in range(1,len(f)):
        s[i] = 1
    for i in range(2,len(f))[::-1]:
        if f[i] <= i:
            s[-1] = f[i-1]-f[i]
        else:
            s.append(f[i-1]-f[i])
    MA = len(s)
    dp = [[0]*MA for i in range(k)]
    dp[0] = [s[i] for i in range(MA)]
    for i in range(MA-1):
        dp[0][i+1] += dp[0][i]
        dp[0][i+1] %= mod
    for l in range(k-1):
        for i in range(1,MA):
            j = MA-i
            dp[l+1][i] += dp[l][j]*s[i]
            dp[l+1][i] %= mod
            dp[l+1][i] += dp[l+1][i-1]
            dp[l+1][i] %= mod
    print(dp[-1][-1])
    return


#Solve
if __name__ == "__main__":
    F()
