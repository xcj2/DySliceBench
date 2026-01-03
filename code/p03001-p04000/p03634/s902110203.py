from collections import defaultdict
import sys,heapq,bisect,math,itertools,string,queue,datetime
sys.setrecursionlimit(10**8)
INF = float('inf')
mod = 10**9+7
eps = 10**-7
AtoZ = [chr(i) for i in range(65,65+26)]
atoz = [chr(i) for i in range(97,97+26)]

def inpl(): return list(map(int, input().split()))
def inpl_s(): return list(input().split())

N = int(input())

lines = defaultdict(set)
for i in range(N-1):
	a,b,c = inpl()
	a -= 1
	b -= 1
	lines[a].add((b,c))
	lines[b].add((a,c))

Q,s = inpl()
s -= 1
ss = [-1]*N
ss[s] = 0

def check(a,w):
	global ss
	for b,c in lines[a]:
		if ss[b] == -1:
			ss[b] = w + c
			check(b,w+c)

check(s,0)

for i in range(Q):
	x,y = inpl()
	print(ss[x-1]+ss[y-1])
