from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N = int(input())
hh = inpl()

ans = 0
def bukatu(hh,L):
    global ans
    if L <= 0:
        return
    elif L == 1:
        ans += hh[0]
        return
    else:
        while not 0 in hh:
            ans += 1
            for i in range(L):
                hh[i] -= 1
        nexthh = [list(map(int,' '.join(h.split('*')).split())) for h in ('*'+'*'.join(map(str,hh))+'*').split('*0*')]
        #print(nexthh,ans)
        for hh in nexthh:
            bukatu(hh,len(hh))

bukatu(hh,N)
print(ans)
