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


n = N
ans = [0]*(N+1)
cnts = [0]*(N+1)

for a in reversed(aa):
    #print(a,n,cnts,ans)
    if cnts[n]%2 == a:
        ans[n] = 0
    else:
        ans[n] = 1
        r = 1
        while r <= math.sqrt(n):
            if n%r == 0:
                cnts[r] += 1
                if r != n//r:
                    cnts[n//r] += 1
            r += 1
    n -= 1


tmp = sum(ans)
if tmp == 0:
    print(0)
else:
    print(tmp)
    fans = []
    for i,x in enumerate(ans):
        if x == 1:
            fans.append(str(i))
    print(' '.join(fans))
