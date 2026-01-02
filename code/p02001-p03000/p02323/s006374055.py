from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N,M = inpl()
lines = defaultdict(set)
for _ in range(M):
    s,t,d = inpl()
    lines[s].add((t,d))


S = 0
dp = [[INF]*N for _ in range(1<<(N+1)-1)]
dp[0][S] = 0
for bit in range(1<<(N+1)-1):
    for s in range(N):
        now = dp[bit][s]
        for t,c in lines[s]:
            if bit & (1<<t): # 訪れたことがある
                continue
            else:
                dp[bit+(1<<t)][t] = min(dp[bit+(1<<t)][t],now+c)

ans = dp[-1][S]
if ans == INF:
    print(-1)
else:
    print(dp[-1][S])

