import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N = I()
    A = LI()
    G = [[] for _ in range(N)]
    dp = [inf for _ in range(N)]
    ans = [0] * N
    for i in range(N-1):
        a, b = LI_()
        G[a].append(b)
        G[b].append(a)

    def update_dp(i):
        j = bisect.bisect_left(dp, A[i])
        before_val = dp[j]
        dp[j] = A[i]
        return j, before_val

    visited = set()

    def dfs(v):
        visited.add(v)

        j = bisect.bisect_left(dp, A[v])
        before_val = dp[j]
        dp[j] = A[v]

        ans[v] = bisect.bisect_left(dp, inf)
        for next_v in G[v]:
            if next_v in visited:
                continue
            dfs(next_v)

        # restore dp
        dp[j] = before_val

    dfs(0)
    for a in ans:
        print(a)

main()

