
from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))
def inpl_str(): return list(sys.stdin.readline().split())

N = inp()
lines = defaultdict(set)
ABs = []
for _ in range(N-1):
    a,b = inpl()
    a,b = a-1, b-1
    ABs.append((a,b))
    lines[a].add(b)
    lines[b].add(a)


K = -1
ki = -1
for i in range(N):
    if K < len(lines[i]):
        K = len(lines[i])
        ki = i



colors = [defaultdict(int) for _ in range(N)]

def dfs(s,bs,bk):
    cnt = 0
    for t in lines[s]:
        if t == bs:
            continue
        else:
            if cnt == bk:
                cnt += 1
            colors[s][t] = cnt
            colors[t][s] = cnt
            dfs(t,s,cnt)
            cnt += 1


for i,t in enumerate(lines[ki]):
    colors[ki][t] = i
    colors[t][ki] = i
    dfs(t,ki,i)

print(K)
for a,b in ABs:
    print(colors[a][b]+1)
