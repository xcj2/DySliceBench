from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())


def dfs(s,cnt):
    global ans
    if cnt > 10:
        ans = False
        return
    for t in lines[s]:
        dfs(t,cnt+1)


N = inp()
for _ in range(N):
    H,W = inpl()
    MAP = [['.']*(W+2)] + [['.']+list(input())+['.'] for y in range(H)] + [['.']*(W+2)]

    als = set([])
    almm = [[INF,0,INF,0] for _ in range(30)]
    for y in range(1,H+1):
        for x in range(1,W+1):
            tmp = MAP[y][x]
            if tmp != '.':
                tmp = ord(tmp) - ord('A')
                als.add(tmp)
                almm[tmp][0] = min(almm[tmp][0],x)
                almm[tmp][1] = max(almm[tmp][1],x)
                almm[tmp][2] = min(almm[tmp][2],y)
                almm[tmp][3] = max(almm[tmp][3],y)

    ans = True
    lines = defaultdict(set)
    for a in als:
        xl,xr,yl,yr = almm[a]
        alpha = chr(a+ord('A'))
        for x in range(xl,xr+1):
            for y in range(yl,yr+1):
                if MAP[y][x] == '.':
                    ans = False
                    break
                elif MAP[y][x] != alpha:
                    lines[a].add(ord(MAP[y][x])-ord('A'))

    for a in als:
        dfs(a,0)


    if not ans:
        print('SUSPICIOUS')
    else:
        print('SAFE')

