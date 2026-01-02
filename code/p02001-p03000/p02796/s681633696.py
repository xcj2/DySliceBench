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
XL = [inpl() for _ in range(N)]
XL.sort()

ans = 1
bx, bl = XL[0]
for i in range(1,N):
    nx, nl = XL[i]

    # print(bx,bl,nx,nl)
    if (nx-bx) >= bl+nl:
        bx = nx
        bl = nl
        ans += 1
    else:
        if nx + nl < bx+bl:
            bx = nx
            bl = nl
        else:
            continue



print(ans)
