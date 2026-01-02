
def examC(inf):
    N = I()
    A = []
    A.append(1)
    for i in range(1, 7):
        A.append(6 ** i)
    for i in range(1, 6):
        A.append(9 ** i)
    A.sort()
    dp = [10 * 5 + 10] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        for s in range(len(A)):
            if i - A[s] >= 0:
                dp[i] = min(dp[i - A[s]] + 1, dp[i])
    ans = dp[N]
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

examC(inf)
