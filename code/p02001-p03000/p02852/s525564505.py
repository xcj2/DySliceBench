
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N,M = inpl()
S = list(map(int,list(input())))

cnt = 1
tmp = []
for i in range(1,N+1):
    if S[i] == 0:
        if cnt > M:
            print(-1)
            exit()
        tmp.append(cnt)
        cnt = 1
    else:
        cnt += 1


cnt = 0
ans = []
for d in reversed(tmp):
    if cnt + d <= M:
        cnt += d
    else:
        ans.append(cnt)
        cnt = d

ans.append(cnt)
ans.reverse()

print(' '.join(map(str,ans)))
