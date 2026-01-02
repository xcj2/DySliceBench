from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

def c(n,d):
    return n+d*N

def dfs(s,n):
    global visited
    visited[s][n] = True
    for t in lines[s]:
        if not visited[t][n]:
            dfs(t,n)


while True:
    N = inp()
    if N == 0:
        break
    else:
        days = 30
        nds = [[False]*days for _ in range(N)]
        for n in range(N):
            tmpl = inpl()
            for i in range(1,tmpl[0]+1):
                nds[n][tmpl[i]-1] = True

        lines = defaultdict(set)
        cnt = 0
        for n in range(N):
            for d1 in range(days):
                for d2 in range(d1,days):
                    if nds[n][d1] and nds[n][d2]:
                        lines[c(n,d1)].add(c(n,d2))

        for d in range(days):
            for n1 in range(N):
                for n2 in range(n1,N):
                    if nds[n1][d] and nds[n2][d]:
                        lines[c(n1,d)].add(c(n2,d))
                        lines[c(n2,d)].add(c(n1,d))

        visited = [[False]*N for _ in range(c(N,days))]
        for n in range(N):
            for d in range(days):
                if nds[n][d]:
                    dfs(c(n,d),n)

        #print(visited)

        for b in range(N*days):
            for n in range(N):
                #print(b,n,visited[b][n])
                if visited[b][n]:
                    continue
                else:
                    break
            else:
                print(b//N+1)
                break
        else:
            print(-1)

