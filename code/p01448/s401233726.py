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
MAX = 100005
imos = [0]*MAX
for _ in range(N):
    a,b = inpl()
    imos[a] += 1
    imos[b+1] -= 1

for i in range(1,MAX):
    imos[i] += imos[i-1]

#print(imos[:10])
ans = 0
for i in range(MAX):
    if imos[i] >= i-1:
        ans = max(ans,i-1)
print(ans)

