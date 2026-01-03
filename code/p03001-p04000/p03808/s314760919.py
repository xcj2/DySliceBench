from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N = int(input())
aa = inpl()
MIN,MAX = min(aa),max(aa)
SUM = sum(aa)
S = N*(N+1)//2

def main():
	if SUM%S != 0:
		return 'NO'
	else:
		k = SUM // S
		if MIN < k or k*N < MAX:
			return 'NO'
		tmp = 0
		for i in range(N):
			d = aa[i-1] - aa[i]
			d += k
			if d % N == 0:
				tmp += d//N
			else:
				return 'NO'
		if tmp == k:
			return 'YES'
		else:
			return 'NO'

print(main())
