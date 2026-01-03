from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

N,p = inpl()
aa = inpl()
cnt = [0]*2
for a in aa:
    cnt[a%2] += 1

def P(n, r):
	return math.factorial(n)//math.factorial(n-r)

def C(n, r):
    if r == 0: return 1
    return P(n, r)//math.factorial(r)

if p == 0:
    ans = pow(2,(cnt[0]))
    tmp = 0
    for i in range(0,cnt[1]+1,2):
        tmp += C(cnt[1],i)
    ans *= tmp
else:
    ans = pow(2,(cnt[0]))
    tmp = 0
    for i in range(1,cnt[1]+1,2):
        tmp += C(cnt[1],i)
    ans *= tmp

print(ans)
