from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N,A,B,C = inpl()
ll = [int(input()) for i in range(N)]

def saiki(cnt,a,b,c,MP):
    if cnt == N:
        if a==0 or b==0 or c==0:
            return INF
        MP += abs(a-A) + abs(b-B) + abs(c-C)
        return MP
    else:
        l = ll[cnt]
        if a == 0:
            tmpa = saiki(cnt+1,a+l,b,c,MP)
        else:
            tmpa = saiki(cnt+1,a+l,b,c,MP+10)
        if b == 0:
            tmpb = saiki(cnt+1,a,b+l,c,MP)
        else:
            tmpb = saiki(cnt+1,a,b+l,c,MP+10)
        if c == 0:
            tmpc = saiki(cnt+1,a,b,c+l,MP)
        else:
            tmpc = saiki(cnt+1,a,b,c+l,MP+10)
        tmpd = saiki(cnt+1,a,b,c,MP)
        return min(tmpa,tmpb,tmpc,tmpd)

print(saiki(0,0,0,0,0))
