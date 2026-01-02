from collections import defaultdict,deque
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N,M,Q = inpl()
kukan = []

for i in range(M):#加算
	l,r = inpl()
	kukan.append([r,-1,l])


for i in range(Q):#クエリ
	p,q = inpl()
	kukan.append([q,i,p])

kukan.sort()

bit = [0]*(N+1)
ans = [0]*Q

def BIT_add(a,w):
	global bit
	x = a
	while x <= N:
		bit[x] += w
		x += x & -x

def BIT_sum(a):
	global bit
	tmp = 0
	x = a
	while x > 0:
		tmp += bit[x]
		x -= x & -x
	return tmp

for t,flag,s in kukan:
	if flag == -1: #加算
		BIT_add(s,1)
	else:#クエリ
		ans[flag] = BIT_sum(t)-BIT_sum(s-1)

for a in ans:
	print(a)
