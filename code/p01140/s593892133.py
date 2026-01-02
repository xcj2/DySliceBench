from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())


while True:
    N,M = inpl()
    if N == 0:
        break
    hh = [inp() for _ in range(N)]
    ww = [inp() for _ in range(M)]
    cnts = defaultdict(int)


    rhh = hh[:]
    for i in range(1,N):
        rhh[i] += rhh[i-1]
    rhh.append(0)

    for i in range(N+1):
        for j in range(i+1,N+1):
            tmp = rhh[j-1] - rhh[i-1]
            cnts[tmp] += 1

    rww = ww[:]
    for i in range(1,M):
        rww[i] += rww[i-1]
    rww.append(0)

    ans = 0
    for i in range(M+1):
        for j in range(i+1,M+1):
            tmp = rww[j-1] - rww[i-1]
            ans += cnts[tmp]

    print(ans)

