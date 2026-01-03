from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inp(): return int(input())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())

N,M = inpl()
xx = inpl()
nums = [0]*M
Pairs = [0]*M
ed = defaultdict(int)

for x in xx:
	nums[x%M] += 1
	if ed[x] == 0:
		ed[x] = 1
	else:
		Pairs[x%M]+=1
		ed[x] = 0

ans = 0
ans += nums[0]//2

if M%2 == 0:
	ans += nums[M//2]//2
	for i in range(1,M//2):
		a = nums[i]
		b = nums[M-i]
		if a < b:
			ans += a + min((b-a)//2,Pairs[M-i])
		else:#b < a:
			ans += b + min((a-b)//2,Pairs[i])
else:
	for i in range(1,M//2+1):
		a = nums[i]
		b = nums[M-i]
		if a < b:
			ans += a + min((b-a)//2,Pairs[M-i])
		else:#b < a:
			ans += b + min((a-b)//2,Pairs[i])

print(ans)
