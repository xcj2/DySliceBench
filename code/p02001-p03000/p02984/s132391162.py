from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,copy,time
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpl_str(): return list(input().split())

N = inp()
aa = inpl()
#aa = [a*2 for a in aa]
S = sum(aa)//2

tmp = 0
raa_ev = [0]
for i in range(1,N,2):
    tmp += aa[i]
    raa_ev.append(tmp)

tmp = 0
raa_od = [0]
for i in range(0,N,2):
    tmp += aa[i]
    raa_od.append(tmp)

ans = [0]*N
for i in range(1,N+1):
    tmp = S
    if i%2 == 1:
        tmp -= raa_od[(i-1)//2]
        tmp -= raa_ev[-1] - raa_ev[(i-1)//2]
    else:
        tmp -= raa_ev[i//2-1]
        tmp -= raa_od[-1] - raa_od[i//2]
    ans[i-1] = tmp*2

print(' '.join(map(str,ans)))
