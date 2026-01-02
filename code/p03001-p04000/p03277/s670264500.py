from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

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

def calc(x):
	aa_dush = [-1]*N
	for i in range(N):
		if aa[i] >= x:
			aa_dush[i] = 1
	#aa_dush = [1, 1, 1, 1, 1, 1, -1, 1, -1, -1]

	S = [0] #S_0 = 0を忘れずにつける
	tmp = 0
	MIN = MAX = 0
	for i in range(N):
		tmp += aa_dush[i]
		MIN = min(tmp,MIN)
		MAX = max(tmp,MAX)
		S.append(tmp)
	#S = [0, 1, 2, 3, 4, 5, 6, 5, 6, 5, 4]
	#MIN = 0 , MAX = 6

	L = (MAX-MIN+1) #BITのサイズ L=6
	bit = [0]*(L+1) #1indexで扱うのでL+1の長さで取る
	ans = 0
	for S_i in S:
		S_i -= (MIN-1) #S_iの最小値が1となるように調整

		#BITで既出の要素のうちS_i以下の要素数をカウント
		tmp = 0
		x = S_i
		while x > 0:
			tmp += bit[x]
			x -= x & -x
		ans += tmp

		#BITのS_iに1を加算して更新
		x = S_i
		while x <= L:
			bit[x] += 1
			x += x & -x

	return ans #中央値がx以上となる(l,r)の組の数

border = ( (N+1)*N//2 +1 )//2
OK = 0
NG = 10**9+3

while NG - OK > 1:
	mid = (OK+NG)//2
	if calc(mid) >= border:
		OK = mid
	else:
		NG = mid

print(OK)
