def examA():
    X, Y = LI()
    ans = X + Y//2
    print(ans)
    return

def examB():
    N = I()
    T, A = LI()
    H = LI()
    cur = 10**9; ans = 0
    for i in range(N):
        now = abs(A - (T - H[i]*0.006))
        if cur>now:
            cur = now
            ans = i
    print(ans+1)
    return

def examC():
    N, M = LI()
    PY = [[]for _ in range(M)]
    d = defaultdict(int)
    ans = [[]for _ in range(M)]
    for i in range(M):
        PY[i] = LI()
        PY[i].append(i)
    PY.sort(key=lambda x:x[1])
    for p,y,s in PY:
        d[p] +=1
        cur = str(p).zfill(6) + str(d[p]).zfill(6)
        ans[s] = cur
    for v in ans:
        print(v)
    return

def examD():
    global mod
    H, W, K = LI()
    fibo = [1]*(W+1)
    for i in range(W-1):
        fibo[i+2] = fibo[i+1] + fibo[i]
    dp = [[0]*(W) for _ in range(H+1)]
    dp[0][0] = 1
#    print(fibo)
    for i in range(H):
        for j in range(W):
            dp[i+1][j] += dp[i][j]*fibo[j]*fibo[W-j-1]%mod
            dp[i+1][j] %=mod
            if j-1>=0:
                dp[i+1][j-1] += dp[i][j]*fibo[j-1]*fibo[W-j-1]%mod
                dp[i+1][j-1] %=mod
            if j+1<W:
                dp[i+1][j+1] += dp[i][j]*fibo[j]*fibo[W-j-2]%mod
                dp[i+1][j+1] %=mod
    ans = dp[H][K-1]
    print(ans)
#    print(dp)
    return

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

if __name__ == '__main__':
    examD()
