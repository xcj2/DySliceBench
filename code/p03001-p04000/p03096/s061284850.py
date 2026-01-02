def examB(mod):
    N = I(); C = [I() for _ in range(N)]
    dp = [0]*(N); dp[0] = 1
    cur = [0]*(max(C)+1); cur[C[0]] =1
    for i in range(1,N):
        if C[i]==C[i-1]:
            dp[i] = dp[i-1]
        else:
            dp[i] = cur[C[i]] + dp[i-1]
            dp[i] %=mod
            cur[C[i]] = dp[i]
#    print(dp)
    ans = dp[-1]%mod
    print(ans)

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
    examB(mod)
