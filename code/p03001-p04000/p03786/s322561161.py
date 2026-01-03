from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N = int(input())
aa = inpl()
aa.sort()

tmp = 0
SUM_aa = [0]
for a in aa:
	tmp += a
	SUM_aa.append(tmp)

def solve(ind):
	size = SUM_aa[ind]
	b_ind = ind

	while True:
		ind = bisect.bisect_right(aa,size*2)

		if ind == N:		#全部吸収
			return True
		elif b_ind == ind:	#ind変更なし
			return False

		size = SUM_aa[ind]
		b_ind = ind

NG = 0
OK = N

while OK-NG > 1:
	mid = (OK+NG)//2
	if solve(mid):
		OK = mid
	else:
		NG = mid

print(N-OK+1)
